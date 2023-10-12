import { elementToBlock, uuidv4 } from "./Shared.js";
import { UDPPApi } from "../API/UDPPApi.js";
export class Block {
    SetDataName(_name) {
        this.data["name"] = _name;
    }
    GetDataName() {
        return this.data["name"];
    }
    SetGroup(_name) {
        this.data["group"] = _name;
    }
    GetGroup() {
        return this.data["group"];
    }
    InsertProperty(_name, _type, _value, _id) {
        console.log(_name, _type, _value);
        console.log(this.properties);
        // @ts-ignore
        this.properties[_name] = {
            type: _type,
            id: _id,
            value: _value,
            block_name: this.uuid
        };
        this.SetProperties(this.properties);
        console.log(this.properties);
        //this.SetProperties({'name': p});
    }
    SetProperties(properties) {
        this.properties = properties;
        for (const prop in this.properties) {
            this.properties[prop].setValue = (val) => {
                if (val === null)
                    return;
                this.properties[prop].value = val;
                this.OnPropertyChanged(prop);
            };
        }
        // Let all props know they changed
        for (const prop in this.properties) {
            this.OnPropertyChanged(prop);
        }
        // Refresh the properties
        this.inspector.refreshProperties();
    }
    DeepCopyProperties() {
        let copy = {};
        for (const prop in this.properties) {
            const propValue = this.properties[prop];
            const propCopy = {
                type: propValue.type,
                value: JSON.parse(JSON.stringify(propValue.value)),
                id: propValue.id
            };
            copy[prop] = propCopy;
        }
        return copy;
    }
    constructor(inspector, _id) {
        // The position of the block in the workspace
        this.position = [0, 0];
        // The scale of the block
        this.scale = 1;
        this.cachedValue = [];
        this.isDirty = true;
        this.data = {
            "name": "",
            "group": "default"
        };
        this.properties = {};
        if (inspector === null)
            throw new Error("Inspector cannot be null!");
        this.inspector = inspector;
        if (_id === undefined || _id == null || _id.length <= 0) {
            this.uuid = uuidv4();
        }
        else {
            this.uuid = _id;
        }
        // Execute the code on the input
        this.promise = (input) => {
            // Execute the Copy property
            const code = this.properties["Code"].value;
            // Function(..) the code and return the result
            let output = Function("input", code)(input);
            // If the output is not an array, wrap it in one
            if (!Array.isArray(output))
                output = [output];
            return Promise.resolve(output);
        };
        this.inputs = [];
        this.outputs = [];
        this.size = [100, 100];
        this.element = this.CreateBlockHTML(0, 0);
        elementToBlock.set(this.element, this);
        for (const prop in this.properties) {
            this.properties[prop].setValue = (val) => {
                if (val === null)
                    return;
                this.properties[prop].value = val;
                this.OnPropertyChanged(prop);
            };
        }
    }
    // Call this method whenever an input or property changes
    SetDirty() {
        this.isDirty = true;
        // Also mark downstream nodes as dirty
        for (let output of this.outputs) {
            for (let edge of output.edges) {
                edge.endSocket.owner.SetDirty();
            }
        }
    }
    OnPropertyChanged(propertyName) {
        const key = propertyName;
        const value = this.properties[propertyName].value;
        const id = this.properties[propertyName].id;
        console.log(`Property ${propertyName} changed! New value: ${this.properties[propertyName].value}`);
        // If the 'Name' property changes, update the title of the block
        let resp = UDPPApi.updateInspectorParameter(this.GetGroup(), this.uuid, id, value);
        this.SetDirty();
    }
    OnSelected() {
        this.element.classList.add('selected');
        this.inspector.selectNode(this);
    }
    OnDeselected() {
        this.inspector.deselectNode();
        this.element.classList.remove('selected');
    }
    AddInputSocket(socket, _id) {
        socket.SetId(_id);
        this.inputs.push(socket);
        let socketElement = socket.GetElement();
        let nodeHeight = this.size[1];
        let socketHeight = socket.size[1];
        let spacing = (nodeHeight - ((this.inputs.length) * socketHeight)) / (this.inputs.length + 1);
        for (let i = 0; i < this.inputs.length; i++) {
            this.inputs[i].element.style.top = ((i + 1) * (spacing + socketHeight)) + 'px';
        }
        this.element.appendChild(socketElement);
    }
    AddOutputSocket(socket, _id) {
        socket.SetId(_id);
        this.outputs.push(socket);
        let socketElement = socket.GetElement();
        let nodeHeight = this.size[1];
        let socketHeight = socket.size[1];
        let spacing = (nodeHeight - ((this.outputs.length) * socketHeight)) / (this.outputs.length + 1);
        for (let i = 0; i < this.outputs.length; i++) {
            this.outputs[i].element.style.top = ((i + 1) * (spacing + socketHeight)) + 'px';
        }
        this.element.appendChild(socketElement);
    }
    AddOrSetTitle(title) {
        if (this.element.querySelector('.title')) {
            // set text
            this.element.querySelector('.title').innerHTML = title;
            return;
        }
        let titleElement = document.createElement('div');
        titleElement.className = 'title';
        titleElement.innerHTML = title;
        this.element.appendChild(titleElement);
    }
    GetTitle() {
        let title = this.element.querySelector('.title').innerHTML;
        if (!title || title.length <= 0) {
            title = this.GetDataName();
            this.AddOrSetTitle(title);
        }
        return title;
    }
    async Evaluate(outputPort = 0) {
        // Evaluate upstream nodes first
        let promises = [];
        for (let input of this.inputs) {
            for (let edge of input.edges) {
                promises.push(edge.startSocket.owner.Evaluate(edge.startSocket.socketNumber));
            }
        }
        let inputValues = await Promise.all(promises);
        if (!this.isDirty && this.cachedValue !== null) {
            // If the node is not dirty and has a cached value, return the cached value
            return this.cachedValue[outputPort];
        }
        // Execute the promise of the current node
        this.element.classList.add('node-executing');
        this.cachedValue = await this.promise(inputValues);
        this.element.classList.remove('node-executing');
        // Mark the node as not dirty
        this.isDirty = false;
        if (this.cachedValue !== null && this.cachedValue !== undefined && this.cachedValue.length > outputPort) {
            console.log(`Output: ${this.cachedValue[outputPort]}`);
            return this.cachedValue[outputPort];
        }
        return [];
    }
    CreateBlockHTML(x, y) {
        let newBlock = document.createElement('div');
        newBlock.className = 'node';
        newBlock.style.width = this.size[0] + 'px';
        newBlock.style.height = this.size[1] + 'px';
        newBlock.style.left = x + 'px';
        newBlock.style.top = y + 'px';
        // Set position
        this.position = [x, y];
        newBlock.id = this.uuid;
        this.element = newBlock;
        return newBlock;
    }
    GetElement(x, y) {
        this.element.style.left = x + 'px';
        this.element.style.top = y + 'px';
        this.element.style.width = this.size[0] + 'px';
        this.element.style.height = this.size[1] + 'px';
        this.position = [x, y];
        return this.element;
    }
    GetProperties() {
        return this.properties;
    }
    Destroy() {
        for (let socket of this.inputs) {
            socket.Destroy();
        }
        for (let socket of this.outputs) {
            socket.Destroy();
        }
        elementToBlock.delete(this.element);
    }
}
