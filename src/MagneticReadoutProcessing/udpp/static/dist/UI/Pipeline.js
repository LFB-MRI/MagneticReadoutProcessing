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
    load_set_pipeline() {
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
        console.log("load_set_pipeline using:");
        console.log("pipeline", OptionPanel.GetPipelineName());
        console.log("api", OptionPanel.GetApiEndpoint());
        // CLEAR EXISTING NODES
        (_a = this.nodeGraph) === null || _a === void 0 ? void 0 : _a.Reset();
        // load pipeline json object from api
        const resolve_pipeline = UDPPApi.getPipeline(OptionPanel.GetPipelineName(), OptionPanel.GetApiEndpoint());
        Promise.resolve(resolve_pipeline).then((pipeline) => {
            var _a;
            const stage = pipeline.stages[0];
            console.log(stage);
            for (let i = 0; i < pipeline.stages.length; i++) {
                (_a = this.nodeGraph) === null || _a === void 0 ? void 0 : _a.CreatePipelineBlock(pipeline.stages[i]);
            }
        });
    }
}
