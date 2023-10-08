import {OptionPanel} from "./OptionPanel.js";
import {PipelineRoot, PipelineStages, UDPPApi} from "../API/UDPPApi.js";
import {NodePanel} from "./NodePanel.js";
import {Block} from "./Block.js";
import {Socket} from "./Socket.js";
import {nodePanel, SocketType} from "./Shared.js";
import {InspectorPanel} from "./InspectorPanel.js";
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


    load_set_pipeline(){
        if(this.nodeGraph === undefined || this.nodeGraph === null){
            throw Error("nodeGraph is undefined");
        }

        if(this.insepctorPanel === undefined || this.insepctorPanel === null){
            throw  Error("insepctorPanel is none");
        }

        if(this.nodeGraph === undefined || this.nodeGraph === null){
            throw  Error("nodeGraph is none");
        }




        console.log("load_set_pipeline using:")
        console.log("pipeline", OptionPanel.GetPipelineName())
        console.log("api", OptionPanel.GetApiEndpoint())


        // load pipeline json object from api
        const resolve_pipeline = UDPPApi.getPipeline(OptionPanel.GetPipelineName(), OptionPanel.GetApiEndpoint());

       Promise.resolve(resolve_pipeline).then((pipeline: PipelineRoot) => {
            const stage  = pipeline.stages[0]
            console.log(stage)
            for (let i = 0; i < pipeline.stages.length; i++) {
                this.nodeGraph?.CreatePipelineBlock(pipeline.stages[i]);
            }
        });




    }


}