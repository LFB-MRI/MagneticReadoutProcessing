// --- IMPORTS ---
import { InspectorPanel } from './UI/InspectorPanel.js';
import { NodePanel } from './UI/NodePanel.js';
import { nodePanel } from './UI/Shared.js';
// Initialize the app
let inspector = new InspectorPanel();
let nodeGraph = new NodePanel(nodePanel, inspector);
//let options: OptionPanel = new OptionPanel(cogIcon, optionPanel);
