export class InspectorPanel {
    constructor() {
        this.selectedNode = null;
        this.inspectorElement = document.getElementById("inspector");
        this.propertyContainer = document.getElementById("inspector-properties");
    }
    selectNode(node) {
        this.selectedNode = node;
        this.refreshProperties();
        this.inspectorElement.classList.remove("inspector-closed");
        this.inspectorElement.classList.add("inspector-open");
    }
    deselectNode() {
        this.selectedNode = null;
        this.inspectorElement.classList.remove("inspector-open");
        this.inspectorElement.classList.add("inspector-closed");
    }
    refreshProperties() {
        this.propertyContainer.innerHTML = '';
        if (this.selectedNode) {
            let headline = document.createElement("p");
            headline.innerHTML = "<h3>" + this.selectedNode.GetTitle() + "</h3><br />";
            this.propertyContainer.appendChild(headline);
            for (const [key, prop] of Object.entries(this.selectedNode.GetProperties())) {
                const propDiv = document.createElement('div');
                //propDiv.textContent = key + " [" + prop.type +"]";
                //propDiv.
                let label_for = document.createElement('label');
                let element_id = prop.block_name + ":" + prop.id + ":" + prop.type;
                console.log(element_id);
                label_for.htmlFor = element_id;
                label_for.textContent = key + " [" + prop.type + "]";
                propDiv.appendChild(label_for);
                switch (prop.type) {
                    case 'int':
                        const number = document.createElement('input');
                        number.id = element_id;
                        number.type = 'number';
                        number.step = '1';
                        number.value = prop.value;
                        number.oninput = (e) => {
                            if (prop.setValue !== undefined) {
                                prop.setValue(e.target.value);
                            }
                        };
                        propDiv.appendChild(number);
                        break;
                    case 'float':
                        const float = document.createElement('input');
                        float.type = 'number';
                        float.id = element_id;
                        float.step = '0.01';
                        float.value = prop.value.toString();
                        float.oninput = (e) => {
                            if (prop.setValue !== undefined) {
                                prop.setValue(e.target.value);
                            }
                        };
                        propDiv.appendChild(float);
                        break;
                    case 'bool':
                        const bool = document.createElement('input');
                        bool.type = 'number';
                        bool.id = element_id;
                        bool.step = '1';
                        bool.min = '0';
                        bool.max = '1';
                        if (prop.value === "1" || prop.value.toString().toLowerCase().includes('t')) {
                            bool.value = '1';
                        }
                        else {
                            bool.value = '0';
                        }
                        bool.oninput = (e) => {
                            if (prop.setValue !== undefined) {
                                prop.setValue(e.target.value);
                            }
                        };
                        propDiv.appendChild(bool);
                        break;
                    default:
                        const str = document.createElement('input');
                        str.type = 'text';
                        str.id = element_id;
                        str.value = prop.value;
                        str.oninput = (e) => {
                            if (prop.setValue !== undefined) {
                                prop.setValue(e.target.value);
                            }
                        };
                        propDiv.appendChild(str);
                }
                this.propertyContainer.appendChild(propDiv);
            }
        }
    }
}
