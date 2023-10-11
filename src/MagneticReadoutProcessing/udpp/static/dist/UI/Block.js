import { elementToBlock, uuidv4 } from "./Shared.js";
export class Block {
    SetDataName(_name) {
        this.data["name"] = _name;
    }
    GetDataName() {
        return this.data["name"];
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
                value: JSON.parse(JSON.stringify(propValue.value))
            };
            copy[prop] = propCopy;
        }
        return copy;
    }
    constructor(inspector) {
        // The position of the block in the workspace
        this.position = [0, 0];
        // The scale of the block
        this.scale = 1;
        this.cachedValue = [];
        this.isDirty = true;
        this.data = {
            "name": ""
        };
        this.properties = {};
        if (inspector === null)
            throw new Error("Inspector cannot be null!");
        this.inspector = inspector;
        this.uuid = uuidv4();
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
        console.log(`Property ${propertyName} changed! New value: ${this.properties[propertyName].value}`);
        // If the 'Name' property changes, update the title of the block
        if (propertyName === 'Name') {
            this.AddOrSetTitle(this.properties[propertyName].value);
        }
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
    AddInputSocket(socket) {
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
    AddOutputSocket(socket) {
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
