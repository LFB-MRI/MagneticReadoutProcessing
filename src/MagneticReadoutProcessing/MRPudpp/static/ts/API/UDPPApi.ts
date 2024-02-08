

export interface PipelineConnectionInformationPoints{
    stage_name: string;
    parameter_name: string;
}
export interface PipelineConnectionInformation{
    from: PipelineConnectionInformationPoints;
    to: PipelineConnectionInformationPoints;
}


export interface PipelineRoot {
    settings: PipelineSettings;
    stages: PipelineStages[];
    connections: PipelineConnectionInformation[];
}

interface PipelineSettings {
    enabled: boolean;
    export_intermediate_results: boolean;
    name: string;
}

interface PipelineStagePosition{
    x: number;
    y: number;
}
export interface PipelineStages {
    function: string;
    name: string;
    position: PipelineStagePosition;
    parameters: PipelineStageParameter[];
    inspector_parameters: PipelineStageParameter[];
    returns: PipelineStageParameter[];
}

export interface PipelineStageParameter {
    direction: string;
    name: string;
    type: string;
    value: string;
    id: string;
}

export interface NodeTypes {
    nodes: string[];
}



export interface PipelineListEntry{
    file: string;
    name: string;

}
export interface PipelineList{
    pipelines: PipelineListEntry[];
}

export class UDPPApi {

    static async getNodeInformation(_function_name:string, _apiendpoint: string = "http://127.0.0.1:5555/api") : Promise<PipelineStages>{
        if (!_apiendpoint.endsWith("/")) {
            _apiendpoint += "/";
        }

        if (!_apiendpoint.startsWith("http://")) {
            _apiendpoint = "http://" + _apiendpoint;
        }


        let url: string = _apiendpoint + "getnodeinformation/" + encodeURIComponent(_function_name);

        console.log(url);
        const response: Response = await fetch(url, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            //mode: 'no-cors',
            cache: "no-cache",
            redirect: "follow"
        });
        console.log(response);
        if (!response.ok) {
            throw new Error('No response generated. !ok');
        }
        if (response.body === null) {
            throw new Error('No response generated. bdy==null');
        }

        let node: PipelineStages = await response.json();
        console.log(node);
        return node;
    }

    static async getNodeTypes(_apiendpoint: string = "http://127.0.0.1:5555/api") : Promise<NodeTypes>{
        if (!_apiendpoint.endsWith("/")) {
            _apiendpoint += "/";
        }

        if (!_apiendpoint.startsWith("http://")) {
            _apiendpoint = "http://" + _apiendpoint;
        }


        let url: string = _apiendpoint + "getnodetypes";

        console.log(url);
        const response: Response = await fetch(url, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            //mode: 'no-cors',
            cache: "no-cache",
            redirect: "follow"
        });
        console.log(response);
        if (!response.ok) {
            throw new Error('No response generated. !ok');
        }
        if (response.body === null) {
            throw new Error('No response generated. bdy==null');
        }

        let nodelist: NodeTypes = await response.json();

        console.log(nodelist);

        return nodelist;
    }

    static async getPipeline(_pipelinename: string, _apiendpoint: string = "http://127.0.0.1:5555/api"): Promise<PipelineRoot> {

        if (!_apiendpoint.endsWith("/")) {
            _apiendpoint += "/";
        }

        if (!_apiendpoint.startsWith("http://")) {
            _apiendpoint = "http://" + _apiendpoint;
        }


        let url: string = _apiendpoint + "getpipeline/" + encodeURIComponent(_pipelinename) + '?canvas_size_x=' + window.innerWidth + '&canvas_size_y=' +  window.innerHeight;

        console.log(url);
        const response: Response = await fetch(url, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            //mode: 'no-cors',
            cache: "no-cache",
            redirect: "follow"
        });
        console.log(response);
        if (!response.ok) {
            throw new Error('No response generated. !ok');
        }
        if (response.body === null) {
            throw new Error('No response generated. bdy==null');
        }

        let pipeline: PipelineRoot = await response.json();

        console.log(pipeline);

        return pipeline;
    }

    static async getListPipelines(_apiendpoint: string = "http://127.0.0.1:5555/api"): Promise<PipelineList>{
        if (!_apiendpoint.endsWith("/")) {
            _apiendpoint += "/";
        }

        if (!_apiendpoint.startsWith("http://")) {
            _apiendpoint = "http://" + _apiendpoint;
        }


        let url: string = _apiendpoint + "listpipelines";

        console.log(url);
        const response: Response = await fetch(url, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            //mode: 'no-cors',
            cache: "no-cache",
            redirect: "follow"
        });
        console.log(response);
        if (!response.ok) {
            throw new Error('No response generated. !ok');
        }
        if (response.body === null) {
            throw new Error('No response generated. bdy==null');
        }

        let pipelines: PipelineList = await response.json();

        console.log(pipelines);

        return pipelines;
    }


    static async updateInspectorParameter(_pipeline:string, _stagename: string, _parameter: string, _value:string,_apiendpoint: string = "http://127.0.0.1:5555/api") : Promise<PipelineStages>{
        if (!_apiendpoint.endsWith("/")) {
            _apiendpoint += "/";
        }

        if (!_apiendpoint.startsWith("http://")) {
            _apiendpoint = "http://" + _apiendpoint;
        }




        let url: string = _apiendpoint + "updateinspectorparameter/" + encodeURIComponent(_pipeline) + "/" + encodeURIComponent(_stagename) + "/" + encodeURIComponent(_parameter) + "/" + encodeURIComponent(_value);

        console.log(url);
        const response: Response = await fetch(url, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            //mode: 'no-cors',
            cache: "no-cache",
            redirect: "follow"
        });
        console.log(response);
        if (!response.ok) {
            throw new Error('No response generated. !ok');
        }
        if (response.body === null) {
            throw new Error('No response generated. bdy==null');
        }

        let node: PipelineStages = await response.json();
        console.log(node);
        return node;
    }



}