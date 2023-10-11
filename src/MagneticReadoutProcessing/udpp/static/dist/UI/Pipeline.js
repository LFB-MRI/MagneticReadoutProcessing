import { OptionPanel } from "./OptionPanel.js";
import { UDPPApi } from "../API/UDPPApi.js";
export class Pipeline {
    constructor() {
    }
    set_node_panel(_nodeGraph) {
        this.nodeGraph = _nodeGraph;
    }
    set_insepctor_panel(_inspectorPanel) {
        this.insepctorPanel = _inspectorPanel;
    }
    static getInstance() {
        if (!Pipeline.instance) {
            Pipeline.instance = new Pipeline();
        }
        return Pipeline.instance;
    }
    load_set_pipeline(_str = "") {
        var _a;
        if (this.nodeGraph === undefined || this.nodeGraph === null) {
            throw Error("nodeGraph is undefined");
        }
        if (this.insepctorPanel === undefined || this.insepctorPanel === null) {
            throw Error("insepctorPanel is none");
        }
        if (this.nodeGraph === undefined || this.nodeGraph === null) {
            throw Error("nodeGraph is none");
        }
        if (_str === "") {
            _str = OptionPanel.GetPipelineName();
        }
        console.log("load_set_pipeline using:");
        console.log("pipeline", OptionPanel.GetPipelineName());
        console.log("api", OptionPanel.GetApiEndpoint());
        // CLEAR EXISTING NODES
        (_a = this.nodeGraph) === null || _a === void 0 ? void 0 : _a.Reset();
        console.log(this.nodeGraph);
        // load pipeline json object from api
        const resolve_pipeline = UDPPApi.getPipeline(_str, OptionPanel.GetApiEndpoint());
        Promise.resolve(resolve_pipeline).then((pipeline) => {
            var _a, _b, _c;
            const stage = pipeline.stages[0];
            console.log(stage);
            // CREATE NODES
            for (let i = 0; i < pipeline.stages.length; i++) {
                (_a = this.nodeGraph) === null || _a === void 0 ? void 0 : _a.CreatePipelineBlock(pipeline.stages[i]);
            }
            // CREATE CONNECTIONS
            for (let i = 0; i < pipeline.connections.length; i++) {
                const connection = pipeline.connections[i];
                console.log("connection:", connection.from.stage_name, " : ", connection.from.parameter_name, "=>", connection.to.stage_name, " : ", connection.to.parameter_name);
                // GET HTML ELEMENT OF SOURCE BLOCK
                let source_block = (_b = this.nodeGraph) === null || _b === void 0 ? void 0 : _b.GetBlockByName(connection.from.stage_name);
                console.log("source_block", source_block);
                let target_block = (_c = this.nodeGraph) === null || _c === void 0 ? void 0 : _c.GetBlockByName(connection.to.stage_name);
                console.log("target_block", target_block);
                if (source_block === null || target_block === null) {
                    return;
                }
                var source_socket;
                // @ts-ignore
                if (connection.from.parameter_name == "return" && (source_block === null || source_block === void 0 ? void 0 : source_block.outputs.length) > 0) {
                    source_socket = source_block === null || source_block === void 0 ? void 0 : source_block.outputs[0];
                }
                else {
                    //source_socket
                }
                console.log("source_socket", source_socket);
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
        });
    }
}
