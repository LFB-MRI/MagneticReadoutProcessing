import {OptionPanel} from "./OptionPanel.js";
import {PipelineConnectionInformation, PipelineRoot, PipelineStages, UDPPApi, PipelineConnectionInformationPoints} from "../API/UDPPApi.js";
import {NodePanel} from "./NodePanel.js";
import {Block} from "./Block.js";
import {Socket} from "./Socket.js";
import {nodePanel, SocketType, ToSocket} from "./Shared.js";
import {InspectorPanel} from "./InspectorPanel.js";
import {Edge} from "./Edge";
export class Pipeline {
    private static instance: Pipeline;

    private static OPTS: OptionPanel;


    private nodeGraph: NodePanel | undefined;
    private insepctorPanel: InspectorPanel | undefined;


    private constructor() {


    }

    public set_node_panel(_nodeGraph: NodePanel){
        this.nodeGraph = _nodeGraph;
    }

    public set_insepctor_panel(_inspectorPanel: InspectorPanel){
        this.insepctorPanel = _inspectorPanel;
    }

    public static getInstance(): Pipeline {
        if (!Pipeline.instance) {
            Pipeline.instance = new Pipeline();
        }

        return Pipeline.instance;
    }


    load_set_pipeline(_str: string = ""){
        if(this.nodeGraph === undefined || this.nodeGraph === null){
            throw Error("nodeGraph is undefined");
        }

        if(this.insepctorPanel === undefined || this.insepctorPanel === null){
            throw  Error("insepctorPanel is none");
        }

        if(this.nodeGraph === undefined || this.nodeGraph === null){
            throw  Error("nodeGraph is none");
        }

        if(_str === ""){
            _str = OptionPanel.GetPipelineName();
        }


        console.log("load_set_pipeline using:")
        console.log("pipeline", OptionPanel.GetPipelineName())
        console.log("api", OptionPanel.GetApiEndpoint())

        // CLEAR EXISTING NODES
        this.nodeGraph?.Reset();

        console.log(this.nodeGraph);

        // load pipeline json object from api
        const resolve_pipeline = UDPPApi.getPipeline(_str, OptionPanel.GetApiEndpoint());

       Promise.resolve(resolve_pipeline).then((pipeline: PipelineRoot) => {
            const stage  = pipeline.stages[0]
            console.log(stage);
           // CREATE NODES
            for (let i = 0; i < pipeline.stages.length; i++) {
                this.nodeGraph?.CreatePipelineBlock(pipeline.stages[i]);
            }

           // CREATE CONNECTIONS
           for (let i = 0; i < pipeline.connections.length; i++) {
                const connection: PipelineConnectionInformation = pipeline.connections[i];

                console.log("connection:" , connection.from.stage_name, " : ", connection.from.parameter_name , "=>", connection.to.stage_name, " : ", connection.to.parameter_name);
                // GET HTML ELEMENT OF SOURCE BLOCK
                let source_block = this.nodeGraph?.GetBlockByName(connection.from.stage_name);
                console.log("source_block", source_block);



               let target_block = this.nodeGraph?.GetBlockByName(connection.to.stage_name);
               console.log("target_block", target_block);


                if(source_block === null || target_block === null){
                    return;
                }

                var source_socket: Socket | undefined;
                // @ts-ignore
               if(connection.from.parameter_name == "return" && source_block?.outputs.length > 0){
                    source_socket = source_block?.outputs[0];
               }else{
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
        });




    }


}