// --- IMPORTS ---
import { Block } from './Block.js';
import { Socket } from './Socket.js';
import { Edge } from './Edge.js';
import { InspectorPanel } from './InspectorPanel.js';
import { SocketType, ToBlock, ToSocket, nodeConnections, contextMenu, nodePanel, workspace, elementToBlock } from './Shared.js';
import {
    NodeTypes, PipelineConnectionInformation,
    PipelineList,
    PipelineListEntry, PipelineRoot,
    PipelineStageParameter,
    PipelineStages,
    UDPPApi
} from "../API/UDPPApi.js";
import {OptionPanel} from "./OptionPanel.js";
import {Pipeline} from "./Pipeline.js";

interface Offset {
    top: number;
    left: number;
}

export class NodePanel {
    panel: HTMLElement;
    selectedSocket: Socket | null = null;
    selectedBlock: Block | null = null;
    lastMousePosition: { x: number; y: number } | null = null;
    connectorPath: SVGPathElement | null = null;
    shouldDragNode = false;
    shouldDragGraph = false;
    graphOffset = { x: 0, y: 0 };
    scaleFactor = 1;
    inspector: InspectorPanel | null = null;

    edges: Edge[] = [];
    blocks: Block[] = [];

    constructor(document: HTMLElement, inspector: InspectorPanel) {
        this.panel = document;
        this.inspector = inspector;
        this.AddListeners();
    }

    private AddListeners() {
        this.panel.addEventListener('mousedown', (evt) => this.OnLeftClickDown(evt));
        this.panel.addEventListener('mouseup', (evt) => this.OnLeftClickUp(evt));
        this.panel.addEventListener('mousemove', (evt) => this.OnMouseMove(evt));
        this.panel.addEventListener('contextmenu', (evt) => this.OnRightClick(evt));
        this.panel.addEventListener('wheel', (evt) => this.OnMouseWheel(evt));

        // This needs to listen from document, not panel
        document.addEventListener('keydown', (evt) => this.OnKeyDown(evt));
    }

    private GetElementOffset(el: HTMLElement): Offset {
        let _x = 0;
        let _y = 0;
        while (el && !isNaN(el.offsetLeft) && !isNaN(el.offsetTop)) {
            _x += el.offsetLeft - el.scrollLeft;
            _y += el.offsetTop - el.scrollTop;
            el = el.offsetParent as HTMLElement;
        }
        return { top: _y, left: _x };
    }

    private CreateConnection(startSocket: Socket): SVGPathElement {
        const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        path.setAttribute('stroke', startSocket.color);
        path.setAttribute('stroke-width', '3');
        path.setAttribute('fill', 'none');
        path.classList.add('edge');
        nodeConnections.appendChild(path);
        return path;
    }

    private UpdateConnection(path: SVGPathElement, startSocket: Socket, endSocket: Socket | null, event: MouseEvent | null): SVGPathElement {
        const startPos = this.GetElementOffset(startSocket.element);
        const startX = startPos.left;
        const startY = startPos.top;

        let endX: number = 0, endY: number = 0;
        if (endSocket) {
            const endPos = this.GetElementOffset(endSocket.element);
            endX = endPos.left;
            endY = endPos.top;
        } else if (event) {
            endX = event.pageX;
            endY = event.pageY;
        }

        const dx = Math.abs(startX - endX) * 0.5;
        const d = `M ${startX},${startY} C ${startX + dx},${startY} ${endX - dx},${endY} ${endX},${endY}`;
        path.setAttribute('d', d);
        return path;
    }
    public Reset(){
        //REMOVE BLOCKS
        while(nodePanel.childNodes.length > 0) {
            //nodePanel.removeChild(this.blocks[i].GetElement(0,0));
            nodePanel.childNodes.item(0).remove(); //p.remove()

        }
        while(this.blocks.length > 0) {
            this.blocks.pop();
        }


    }

    public CreatePipelineBlock(_description: PipelineStages): Block{
        console.log("CreatePipelineBlock");

        var block = new Block(this.inspector);

        const name: string = _description.name.replace("_", "<br>");
        block.AddOrSetTitle(name);

        block.SetDataName(_description.name)
        // add input sockets
        for (let i = 0; i < _description.parameters.length; i++) {
            const param: PipelineStageParameter = _description.parameters[i];
            block.AddInputSocket(new Socket(block, param.name, param.type, SocketType.INPUT, i));
        }

        //add output sockets => in general just one
        for (let i = 0; i < _description.returns.length; i++) {
            const param: PipelineStageParameter = _description.returns[i];
            block.AddInputSocket(new Socket(block, param.name, param.type, SocketType.OUTPUT, i));
        }



        // add inspector parameter inputs
        //let p: BlockProperty;
        //p.setValue("");
        //block.SetProperties("", p);

        let blockElement = block.GetElement(_description.position.x, _description.position.y);
        nodePanel.appendChild(blockElement);


        return block;
    }

    private async PopulateContextMenu(searchText: string) {
        const list = contextMenu.querySelector('ul')!;
        list.innerHTML = '';
        // fetch node list from api
        var nodeTypes: NodeTypes = await UDPPApi.getNodeTypes(OptionPanel.GetApiEndpoint());
        const pipelines: PipelineList = await UDPPApi.getListPipelines(OptionPanel.GetApiEndpoint());


        const seperator =  "---- PIPELINES ---";
        nodeTypes.nodes.push(seperator);

        for (let i = 0; i < pipelines.pipelines.length; i++) {
            const entry: PipelineListEntry = pipelines.pipelines[i];
            nodeTypes.nodes.push(entry.file)
        }
        console.log(pipelines);


        for (const nodeType of nodeTypes.nodes) {
            if (nodeType.toLowerCase().includes(searchText.toLowerCase())) {
                const listItem = document.createElement('li');
                listItem.textContent = nodeType;

                if(nodeType === seperator) {
                }else if(nodeType.includes(".yaml")){
                    listItem.addEventListener('click', (e) => {
                        this.load_set_pipeline(nodeType.toString(), e.clientX, e.clientY);
                        contextMenu.style.display = 'none';
                    });
                }else{
                    listItem.addEventListener('click', (e) => {
                        this.CreateBlock(nodeType, e.clientX, e.clientY);
                        contextMenu.style.display = 'none';
                    });
                }




                list.appendChild(listItem);
            }
        }
    }

    private async CreateBlock(nodeType: string, _pos_x:number | undefined, _pos_y: number | undefined): Promise<Block> {

        let block_description: PipelineStages = await UDPPApi.getNodeInformation(nodeType, OptionPanel.GetApiEndpoint());
        //set block position to clicked position if given
        if(_pos_x && _pos_y && _pos_x > 0 && _pos_y > 0){
            block_description.position.x = _pos_x;
            block_description.position.y = _pos_y;
        }

        let block = this.CreatePipelineBlock(block_description);
        this.blocks.push(block);
        return block;
    }


    public GetBlockByName(_name: string): (Block| null){
        console.log("GetBlockByName", _name, this.blocks);
        for (let i = 0; i < this.blocks.length; i++) {
            const b: Block = this.blocks[i];
            console.log("b.GetDataName()", b.GetDataName());
            if(b.GetDataName() === _name){
                return b;
            }
        }
        return null;
    }

    private OnLeftClickDown(evt: MouseEvent) {
        // Hide context menu
        contextMenu.style.display = 'none';
        // Return if not a left click
        if (evt.button !== 0) return;

        // SOCKET CLICK START
        if (Socket.IsOutput(evt)) {
            let socket = ToSocket(evt.target as HTMLElement);

            if (socket) {
                console.log("socket", socket);
                this.selectedSocket = socket;
                this.connectorPath = this.CreateConnection(this.selectedSocket);
                console.log(this.connectorPath);
            }
        } else {
            // Select any node
            this.shouldDragNode = true;
            if (this.selectedBlock !== null) {
                this.selectedBlock.OnDeselected();
                this.selectedBlock = null;
            }
        }

        if (this.selectedSocket !== null) return;

        // NODE DRAG START
        if (evt.target instanceof HTMLElement && evt.target.className === 'node') {
            let node = ToBlock(evt.target);
            if (node) {
                this.lastMousePosition = { x: evt.offsetX, y: evt.offsetY };
                this.selectedBlock = node;
                node.OnSelected();
            }
        } else if (evt.target === this.panel) {
            this.shouldDragGraph = true;
            this.lastMousePosition = { x: evt.clientX, y: evt.clientY };
        }
    }

    private OnLeftClickUp(evt: MouseEvent) {
        // Return if not a left click
        if (evt.button !== 0) return;

        this.shouldDragNode = false;
        this.shouldDragGraph = false;

        if (this.selectedSocket !== null) {
            let isInput = Socket.IsInput(evt)

            // If we released on an input socket
            if (isInput) {
                let endSocket = ToSocket(evt.target as HTMLElement);
                if (endSocket && this.connectorPath) {
                    this.connectorPath = this.UpdateConnection(this.connectorPath, this.selectedSocket, endSocket, evt);
                    let edge = new Edge(this.connectorPath, this.selectedSocket, endSocket);


                    // Add the edges
                    this.selectedSocket.Connect(edge);
                    endSocket.Connect(edge);

                    // Add the edge to the list
                    this.edges.push(edge);
                }
            } else {
                // If this socket is the same as the StartSocket, remove any connections
                if (evt.target === this.selectedSocket.element) {
                    this.selectedSocket.DisconnectAll();
                }
            }

            // reset the start socket
            this.selectedSocket = null;

            // destroy the line if we didn't connect it
            if (!isInput) {
                nodeConnections.removeChild(this.connectorPath as Node);
            }
            return;
        }
    }

    private OnRightClick(evt: MouseEvent) {
        // Return if not a right click
        if (evt.button !== 2) return;

        evt.preventDefault();
        if (evt.target instanceof HTMLElement && evt.target.className === 'node') {
            let node = ToBlock(evt.target);
            if (node) {
                node.Evaluate();
                return;
            }
            return;
        }

        if (evt.target instanceof HTMLElement && evt.target.id === 'nodes') {
            evt.preventDefault();
            contextMenu.style.display = 'block';
            contextMenu.style.left = `${evt.clientX}px`;
            contextMenu.style.top = `${evt.clientY}px`;
        } this.PopulateContextMenu('');
    }

    private OnKeyDown(evt: KeyboardEvent) {
        if (evt.key === 'Delete') {
            if (this.selectedBlock !== null) {
                this.selectedBlock.OnDeselected();
                this.selectedBlock.Destroy();
                nodePanel.removeChild(this.selectedBlock.element);
                elementToBlock.delete(this.selectedBlock.element);
                this.blocks.splice(this.blocks.indexOf(this.selectedBlock), 1);
                this.selectedBlock = null;
            }
        }
        // If you hit D with a node selected and the cursor is over the node panel, duplicate the node
        if (evt.key === 'd' && this.selectedBlock !== null) {
            let newBlock = this.CloneBlock(this.selectedBlock);
            this.selectedBlock.OnDeselected();
            this.selectedBlock = null;
            this.blocks.push(newBlock);
            nodePanel.appendChild(newBlock.element);
            this.selectedBlock = newBlock;
            this.selectedBlock.OnSelected();
        }
    }

    private CloneBlock(block: Block): Block {
        let newBlock = new Block(this.inspector);

        // Copy the properties from the original block
        newBlock.SetProperties(block.DeepCopyProperties());

        // Add the inputs
        for (let i in block.inputs) {
            let input = block.inputs[i];
            let index = parseInt(i) + 1;
            newBlock.AddInputSocket(new Socket(newBlock, "Input" + index, input.dataType, input.socketType, input.socketNumber));
        }

        // Add the outputs
        for (let i in block.outputs) {
            let output = block.outputs[i];
            let index = parseInt(i) + 1;
            newBlock.AddOutputSocket(new Socket(newBlock, "Output" + index, output.dataType, output.socketType, output.socketNumber));
        }

        // place the block next to the original block
        newBlock.element.style.left = (parseInt(block.element.style.left) + 20) + 'px';
        newBlock.element.style.top = (parseInt(block.element.style.top) + 20) + 'px';
        // Ontop of the original block
        newBlock.element.style.zIndex = (parseInt(block.element.style.zIndex) + 1) + '';

        elementToBlock.set(newBlock.element, newBlock);
        return newBlock;
    }

    private OnMouseMove(evt: MouseEvent) {
        if (this.selectedSocket !== null && this.connectorPath !== null) {
            this.UpdateConnection(this.connectorPath, this.selectedSocket, null, evt);
        }

        // Drag a node, from where we clicked on it
        if (this.shouldDragNode === true && this.selectedBlock !== null && this.lastMousePosition !== null) {
            let x = evt.pageX - this.lastMousePosition.x;
            let y = evt.pageY - this.lastMousePosition.y;
            let s = this.selectedBlock.scale;

            this.selectedBlock.position[0] = x;
            this.selectedBlock.position[1] = y;
            this.selectedBlock.element.style.left = this.selectedBlock.position[0] + 'px';
            this.selectedBlock.element.style.top = this.selectedBlock.position[1] + 'px';


            this.edges.forEach(edge => {
                this.UpdateConnection(edge.element, edge.startSocket, edge.endSocket, evt);
            });
        }

        // Drag the graph
        if (this.shouldDragGraph) {
            if (this.lastMousePosition === null) return;
            const dx = evt.clientX - this.lastMousePosition.x;
            const dy = evt.clientY - this.lastMousePosition.y;
            this.lastMousePosition = { x: evt.clientX, y: evt.clientY };

            this.blocks.forEach(block => {
                block.position[0] += dx;
                block.position[1] += dy;
                block.element.style.left = block.position[0] + 'px';
                block.element.style.top = block.position[1] + 'px';

                block.outputs.forEach(socket => {
                    socket.edges.forEach(edge => {
                        this.UpdateConnection(edge.element, edge.startSocket, edge.endSocket, null);
                    });
                });

                block.inputs.forEach(socket => {
                    socket.edges.forEach(edge => {
                        this.UpdateConnection(edge.element, edge.startSocket, edge.endSocket, null);
                    });
                });
            });

            // Move background
            workspace.style.backgroundPositionX = (this.graphOffset.x || 0) + dx + 'px';
            workspace.style.backgroundPositionY = (this.graphOffset.y || 0) + dy + 'px';
            this.graphOffset = { x: this.graphOffset.x + dx, y: this.graphOffset.y + dy };
        }
    }

    private OnMouseWheel(evt: WheelEvent) {
        evt.preventDefault();  // Prevent default scrolling

        const zoomSensitivity = -0.001;
        const scaleFactorOld = this.scaleFactor;
        this.scaleFactor *= 1 + evt.deltaY * zoomSensitivity;
        this.scaleFactor = Math.max(this.scaleFactor, 0.25); // Lower bound scale factor as needed
        this.scaleFactor = Math.min(this.scaleFactor, 1); // Upper bound scale factor as needed
        // this.scaleFactor = Math.round(this.scaleFactor * 10) / 10;

        // Calculate cursor position relative to the SVG
        const workspaceRect = workspace.getBoundingClientRect();
        const cursorX = evt.clientX - workspaceRect.left;
        const cursorY = evt.clientY - workspaceRect.top;

        this.blocks.forEach(block => {
            // Calculate new position based on scaling
            const offsetX = cursorX - block.position[0];
            const offsetY = cursorY - block.position[1];
            const dx = offsetX * (1 - this.scaleFactor / scaleFactorOld);
            const dy = offsetY * (1 - this.scaleFactor / scaleFactorOld);
            block.position[0] += dx;
            block.position[1] += dy;

            // Update scale
            block.scale = this.scaleFactor;

            // Update CSS
            block.element.style.left = block.position[0] + 'px';
            block.element.style.top = block.position[1] + 'px';
            block.element.style.transform = `scale(${block.scale})`;
        });

        this.edges.forEach(edge => {
            this.UpdateConnection(edge.element, edge.startSocket, edge.endSocket, evt);
        });

        //  Scale background CSS
        // #workspace {
        //     position: absolute;
        //     width: 100vw;
        //     height: 100vh;
        //     background: #1E1E1E;
        //     background - image: radial - gradient(#484848 1px, transparent 0);
        //     background - size: 40px 40px;
        //     background - position: -19px - 19px;
        // }

        workspace.style.backgroundSize = (40 * this.scaleFactor) + 'px ' + (40 * this.scaleFactor) + 'px';
        this.ApplyScale();
    }

    private ApplyScale() {
        // Get all HTML node elements
        let nodes = this.blocks.map(block => block.element);

        // Apply similar transformation to each HTML node
        for (let i = 0; i < nodes.length; i++) {
            let node = nodes[i];
            node.style.transform = `scale(${this.blocks[i].scale})`;
        }
    }



    private async load_set_pipeline(_str: string = "", base_x: number, base_y: number) {
        //IF  NOT
        if(_str === ""){
            return;
        }

        // FETCH PIPELINE DATA =Y BASICALLY THE YAML FILE
        const pipeline = await UDPPApi.getPipeline(_str, OptionPanel.GetApiEndpoint());
        // CREATE NODES
        for (let i = 0; i < pipeline.stages.length; i++) {
            const stage: PipelineStages = pipeline.stages[i];
            const b: Block = await  this.CreateBlock(stage.function, stage.position.x, stage.position.y);
        }





// CREATE CONNECTIONS
        for (let i = 0; i < pipeline.connections.length; i++) {
            const connection: PipelineConnectionInformation = pipeline.connections[i];

            console.log("connection:", connection.from.stage_name, " : ", connection.from.parameter_name, "=>", connection.to.stage_name, " : ", connection.to.parameter_name);
            // GET HTML ELEMENT OF SOURCE BLOCK
            let source_block = this.GetBlockByName(connection.from.stage_name);
            console.log("source_block", source_block);


            let target_block = this.GetBlockByName(connection.to.stage_name);
            console.log("target_block", target_block);


            if (source_block === null || target_block === null) {
                return;
            }

            var source_socket: Socket | undefined;
            // @ts-ignore
            if (connection.from.parameter_name == "return" && source_block?.outputs.length > 0) {
                source_socket = source_block?.outputs[0];
            } else {
                //source_socket
            }
            console.log("source_socket", source_socket)
            //let endSocket = ToSocket(evt.target as HTMLElement);
            //if (endSocket && this.connectorPath) {
            //    this.connectorPath = this.UpdateConnection(this.connectorPath, this.selectedSocket, endSocket, evt);
            //    let edge = new Edge(this.connectorPath, this.selectedSocket, endSocket);


            // Add the edges
            //    this.selectedSocket.Connect(edge);
            //    endSocket.Connect(edge);

            // Add the edge to the list
            //    this.edges.push(edge);
            //this.nodeGraph?.CreatePipelineBlock(pipeline.stages[i]);
        }


    }
}