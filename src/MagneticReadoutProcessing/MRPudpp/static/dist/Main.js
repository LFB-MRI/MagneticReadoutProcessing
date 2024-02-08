// --- IMPORTS ---
import { InspectorPanel } from './UI/InspectorPanel.js';
import { NodePanel } from './UI/NodePanel.js';
import { OptionPanel } from './UI/OptionPanel.js';
import { Pipeline } from './UI/Pipeline.js';
import { cogIcon, nodePanel, optionPanel } from './UI/Shared.js';
// Initialize the app
let inspector = new InspectorPanel();
// Initialize the pipeline loader
let nodeGraph = new NodePanel(nodePanel, inspector);
let pipeline = Pipeline.getInstance();
pipeline.set_node_panel(nodeGraph);
pipeline.set_insepctor_panel(inspector);
let options = new OptionPanel(cogIcon, optionPanel);
// options panel is used as entry point to load pipeline data in
