import {UDPPApi} from "../API/UDPPApi.js";
import {Pipeline} from "./Pipeline.js";
export class OptionPanel {


    private panel: HTMLElement;
    private pipelineinput: HTMLInputElement;
    private apiendpoint: HTMLInputElement;
    private save_button: HTMLButtonElement;

    private icon: HTMLElement;
    private static API: UDPPApi;




    constructor(icon: HTMLElement, panel: HTMLElement) {
        this.icon = icon;
        this.panel = panel;
        this.pipelineinput = this.panel.querySelector('input#pipelinefile') as HTMLInputElement;
        this.save_button = this.panel.querySelector('#save-pipelinefile') as HTMLButtonElement;
        this.apiendpoint = this.panel.querySelector('input#apiendpoint') as HTMLInputElement;


        // Load PIPELINE
        const queryString: string = window.location.search;
        const urlParams = new URLSearchParams(queryString);

        console.log(urlParams)
        var reload: boolean = false;
        if(urlParams.has('pipeline') && urlParams.get('pipeline') !== OptionPanel.GetPipelineName()){
            this.pipelineinput.setAttribute('value', urlParams.get('pipeline') || "pipeline.yaml");
            reload = true;
        }else if(OptionPanel.GetPipelineName() === ""){
            this.pipelineinput.setAttribute('value', "pipeline.yaml");
        }else{
            this.pipelineinput.setAttribute('value', OptionPanel.GetPipelineName() || "pipeline.yaml");
        }

        if(urlParams.has('apiendpoint') && urlParams.get('apiendpoint') !== OptionPanel.GetApiEndpoint()){
            this.apiendpoint.setAttribute('value', urlParams.get('apiendpoint') || "http://127.0.0.1:5555/api");
            reload = true;
        }else if(OptionPanel.GetApiEndpoint() === ""){
            this.apiendpoint.setAttribute('value', "http://127.0.0.1:5555/api");
            reload = true;
        }else{
            this.apiendpoint.setAttribute('value', OptionPanel.GetApiEndpoint() || "http://127.0.0.1:5555/api");
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

    static GetPipelineName(): string {
        var ret: string | null = sessionStorage.getItem('pipelineinput');
        if(ret == null){
            return "";
        }
        return ret;
    }

    static GetApiEndpoint(): string {
        var ret: string | null = sessionStorage.getItem('apiendpoint');
        if(ret == null){
            return "";
        }
        return ret;
    }
}