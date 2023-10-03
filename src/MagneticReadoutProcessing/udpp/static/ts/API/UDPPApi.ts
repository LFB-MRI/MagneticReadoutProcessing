//import axios from 'axios';
//import { AxiosResponse } from 'axios';



 interface PipelineRoot {
    settings: PipelineSettings;
    stages: PipelineStages[];
};

interface PipelineSettings {
    enabled: boolean;
    export_intermediate_results: boolean;
    name: string;
};

export interface PipelineStages {
    function: string;
    name: string;
    parameters: PipelineStageParameter[];
};

export interface PipelineStageParameter {
    direction: string;
    name: string;
    type: string;
    value: string;
};


export class UDPPApi {



    static async getPipeline(_pipelinename: string, _apiendpoint: string = "http://127.0.0.1:5555/api"): Promise<PipelineRoot> {

        if(!_apiendpoint.endsWith("/")){
            _apiendpoint += "/";
        }

        if(!_apiendpoint.startsWith("http://")){
            _apiendpoint = "http://" + _apiendpoint;
        }


        let url: string = _apiendpoint + "getpipeline/" + _pipelinename;

        console.log(url);
        const response: Response= await fetch(url, {
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
        if (!response.ok) { throw new Error('No response generated. !ok'); }
        if (response.body === null) {throw new Error('No response generated. bdy==null');}


      // let json: object = await response.json();
       //console.log(json)



       let pipeline: PipelineRoot = await response.json();//= Object.create(PipelineRoot.prototype);

      //  Object.assign(pipeline, json);

        console.log(pipeline);

        return pipeline
        // Assuming the response data has a field called 'choices' which is an array containing the generated text.
        //if (response.data.choices && response.data.choices.length > 0) {
        //return response.data.choices[0].text;
        //} else {
        //    throw new Error('No response generated.');
        //}
    }


}