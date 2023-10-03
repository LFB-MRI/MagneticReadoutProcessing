import {UDPPApi} from "../API/UDPPApi.js";
export class OptionPanel {


    private panel: HTMLElement;
    private pipelineinput: HTMLInputElement;
    private apiendpoint: HTMLInputElement;
    private save_button: HTMLButtonElement;
    private load_button: HTMLButtonElement;
    private icon: HTMLElement;
    private static API: UDPPApi;

    constructor(icon: HTMLElement, panel: HTMLElement) {
        this.icon = icon;
        this.panel = panel;
        this.pipelineinput = this.panel.querySelector('input#pipelinefile') as HTMLInputElement;
        this.save_button = this.panel.querySelector('#save-pipelinefile') as HTMLButtonElement;
        this.load_button = this.panel.querySelector('#load-pipelinefile') as HTMLButtonElement;
        this.apiendpoint = this.panel.querySelector('input#apiendpoint') as HTMLInputElement;


        // Load PIPELINE
        const queryString: string = window.location.search;
        const urlParams = new URLSearchParams(queryString);

        console.log(urlParams)
        var reload: boolean = false;
        if(urlParams.has('pipeline') && urlParams.get('pipeline') !== this.GetPipelineName()){
            this.pipelineinput.setAttribute('value', urlParams.get('pipeline') || "pipeline.yaml");
            reload = true;
        }else if(this.GetPipelineName() === ""){
            this.pipelineinput.setAttribute('value', "pipeline.yaml");
        }else{
            this.pipelineinput.setAttribute('value', this.GetPipelineName() || "pipeline.yaml");
        }

        if(urlParams.has('apiendpoint') && urlParams.get('apiendpoint') !== this.GetApiEndpoint()){
            this.apiendpoint.setAttribute('value', urlParams.get('apiendpoint') || "http://127.0.0.1:5555/api");
            reload = true;
        }else if(this.GetApiEndpoint() === ""){
            this.apiendpoint.setAttribute('value', "http://127.0.0.1:5555/api");
            reload = true;
        }else{
            this.apiendpoint.setAttribute('value', this.GetApiEndpoint() || "http://127.0.0.1:5555/api");
        }

        console.log(this.pipelineinput.value);
        console.log(this.apiendpoint.value);

        this.SaveSettings();

        if(reload){
            window.location.reload()
        }
        // Hide panel initially
        this.Hide();

        // Add event listeners
        this.AddListeners();
    }

    AddListeners() {
        // Add event listeners
        this.save_button.addEventListener('mousedown', () => this.SaveSettings());
        this.load_button.addEventListener('mousedown', () =>UDPPApi.getPipeline(this.GetPipelineName(), this.GetApiEndpoint()));


        this.icon.addEventListener('mousedown', (e) => {
            console.log('show');
            if (this.panel.style.display === 'none') {
                this.Show();
            } else {
                this.Hide();
            }
        });
    }

    Show() {
        this.panel.style.display = 'block';
    }

    Hide() {
        this.panel.style.display = 'none';
    }

    SaveSettings() {
        console.log('SaveSettings');
        sessionStorage.setItem('pipelineinput', this.pipelineinput.value);
        sessionStorage.setItem('apiendpoint', this.apiendpoint.value);

        this.Hide();
    }

    GetPipelineName(): string {
        var ret: string | null = sessionStorage.getItem('pipelineinput');
        if(ret == null){
            return "";
        }
        return ret;
    }

    GetApiEndpoint(): string {
        var ret: string | null = sessionStorage.getItem('apiendpoint');
        if(ret == null){
            return "";
        }
        return ret;
    }
}