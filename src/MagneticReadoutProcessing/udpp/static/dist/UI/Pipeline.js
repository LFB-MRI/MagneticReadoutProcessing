import { OptionPanel } from "./OptionPanel.js";
import { UDPPApi } from "../API/UDPPApi.js";
import { Block } from "./Block.js";
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
    load_set_pipeline() {
        if (this.nodeGraph === undefined || this.nodeGraph === null) {
            throw Error("nodeGraph is undefined");
        }
        if (this.insepctorPanel === undefined || this.insepctorPanel === null) {
            throw Error("insepctorPanel is none");
        }
        if (this.nodeGraph === undefined || this.nodeGraph === null) {
            throw Error("nodeGraph is none");
        }
        console.log("load_set_pipeline using:");
        console.log("pipeline", OptionPanel.GetPipelineName());
        console.log("api", OptionPanel.GetApiEndpoint());
        // load pipeline json object from api
        const resolve_pipeline = UDPPApi.getPipeline(OptionPanel.GetPipelineName(), OptionPanel.GetApiEndpoint());
        Promise.resolve(resolve_pipeline).then((pipeline) => {
            const stage = pipeline.stages[0];
            console.log(stage);
            // @ts-ignore
            let block = new Block(this.insepctorPanel);
            block.AddOrSetTitle(`${stage.name} [${stage.function}]`);
            let blockElement = block.GetElement(stage.position.x, stage.position.y);
            //block.CreateBlockHTML()
            // block.AddInputSocket(new Socket(block, 'input1', 'default', SocketType.INPUT, 0));
            // block.AddInputSocket(new Socket(block, 'input2', 'number', SocketType.INPUT, 1));
            // block.AddInputSocket(new Socket(block, 'input3', 'string', SocketType.INPUT, 2));
            // block.AddOutputSocket(new Socket(block, 'output1', 'number', SocketType.OUTPUT, 0));
            // block.AddOutputSocket(new Socket(block, 'output2', 'boolean', SocketType.OUTPUT, 1));
            // @ts-ignore
            this.nodeGraph.blocks.push();
        });
    }
}
