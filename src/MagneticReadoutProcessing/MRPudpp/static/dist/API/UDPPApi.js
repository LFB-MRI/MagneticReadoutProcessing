export class UDPPApi {
    static async getNodeInformation(_function_name, _apiendpoint = "http://127.0.0.1:5555/api") {
        if (!_apiendpoint.endsWith("/")) {
            _apiendpoint += "/";
        }
        if (!_apiendpoint.startsWith("http://")) {
            _apiendpoint = "http://" + _apiendpoint;
        }
        let url = _apiendpoint + "getnodeinformation/" + encodeURIComponent(_function_name);
        console.log(url);
        const response = await fetch(url, {
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
        let node = await response.json();
        console.log(node);
        return node;
    }
    static async getNodeTypes(_apiendpoint = "http://127.0.0.1:5555/api") {
        if (!_apiendpoint.endsWith("/")) {
            _apiendpoint += "/";
        }
        if (!_apiendpoint.startsWith("http://")) {
            _apiendpoint = "http://" + _apiendpoint;
        }
        let url = _apiendpoint + "getnodetypes";
        console.log(url);
        const response = await fetch(url, {
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
        let nodelist = await response.json();
        console.log(nodelist);
        return nodelist;
    }
    static async getPipeline(_pipelinename, _apiendpoint = "http://127.0.0.1:5555/api") {
        if (!_apiendpoint.endsWith("/")) {
            _apiendpoint += "/";
        }
        if (!_apiendpoint.startsWith("http://")) {
            _apiendpoint = "http://" + _apiendpoint;
        }
        let url = _apiendpoint + "getpipeline/" + encodeURIComponent(_pipelinename) + '?canvas_size_x=' + window.innerWidth + '&canvas_size_y=' + window.innerHeight;
        console.log(url);
        const response = await fetch(url, {
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
        let pipeline = await response.json();
        console.log(pipeline);
        return pipeline;
    }
    static async getListPipelines(_apiendpoint = "http://127.0.0.1:5555/api") {
        if (!_apiendpoint.endsWith("/")) {
            _apiendpoint += "/";
        }
        if (!_apiendpoint.startsWith("http://")) {
            _apiendpoint = "http://" + _apiendpoint;
        }
        let url = _apiendpoint + "listpipelines";
        console.log(url);
        const response = await fetch(url, {
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
        let pipelines = await response.json();
        console.log(pipelines);
        return pipelines;
    }
    static async updateInspectorParameter(_pipeline, _stagename, _parameter, _value, _apiendpoint = "http://127.0.0.1:5555/api") {
        if (!_apiendpoint.endsWith("/")) {
            _apiendpoint += "/";
        }
        if (!_apiendpoint.startsWith("http://")) {
            _apiendpoint = "http://" + _apiendpoint;
        }
        let url = _apiendpoint + "updateinspectorparameter/" + encodeURIComponent(_pipeline) + "/" + encodeURIComponent(_stagename) + "/" + encodeURIComponent(_parameter) + "/" + encodeURIComponent(_value);
        console.log(url);
        const response = await fetch(url, {
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
        let node = await response.json();
        console.log(node);
        return node;
    }
}
