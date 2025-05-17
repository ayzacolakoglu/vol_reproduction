/************************* 
 * Vol_Reproduction *
 *************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2024.2.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'vol_reproduction';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 4)}`,
    'prolificID': '',
    'gender (M/F)': '',
    'age': '',
};

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from feedback_code
fb_text = "";

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'pix',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(scale_setupRoutineBegin());
flowScheduler.add(scale_setupRoutineEachFrame());
flowScheduler.add(scale_setupRoutineEnd());
const key_scaleLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(key_scaleLoopBegin(key_scaleLoopScheduler));
flowScheduler.add(key_scaleLoopScheduler);
flowScheduler.add(key_scaleLoopEnd);



flowScheduler.add(InstructionRoutineBegin());
flowScheduler.add(InstructionRoutineEachFrame());
flowScheduler.add(InstructionRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);







flowScheduler.add(GoodbyeRoutineBegin());
flowScheduler.add(GoodbyeRoutineEachFrame());
flowScheduler.add(GoodbyeRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'bank-1300155_640.png', 'path': 'bank-1300155_640.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DATA);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expName}_${expInfo["participant"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var scale_setupClock;
var oldt;
var x_size;
var y_size;
var screen_height;
var x_scale;
var y_scale;
var dbase;
var unittext;
var vsize;
var screen_scale_keysClock;
var text_top;
var text_bottom;
var ccimage;
var rectangle_keysClock;
var rectangle_text;
var polygon_keys;
var key_resp_keys;
var InstructionClock;
var text_inst;
var instr_key;
var practice_count;
var subCond;
var blockClock;
var Block_text;
var showBlockText;
var blockText;
var key_resp;
var EncodingClock;
var stimulus_grating;
var fixation;
var cue_to_reproduceClock;
var rep_cue;
var ReproductionClock;
var gabor;
var feedbackClock;
var showFeedback;
var feedback_text;
var key_resp_2;
var itiClock;
var iti_blank;
var GoodbyeClock;
var goodbye_text;
var goodbye_key;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "scale_setup"
  scale_setupClock = new util.Clock();
  // Run 'Begin Experiment' code from scale_code
  oldt = 0;
  x_size = 8.56;
  y_size = 5.398;
  screen_height = 0;
  if ((psychoJS.window.units === "norm")) {
      x_scale = 0.05;
      y_scale = 0.1;
      dbase = 0.0001;
      unittext = " norm units";
      vsize = 2;
  } else {
      if ((psychoJS.window.units === "pix")) {
          x_scale = 60;
          y_scale = 40;
          dbase = 0.1;
          unittext = " pixels";
          vsize = psychoJS.window.size[1];
      } else {
          x_scale = 0.05;
          y_scale = 0.05;
          dbase = 0.0001;
          unittext = " height units";
          vsize = 1;
      }
  }
  
  // Initialize components for Routine "screen_scale_keys"
  screen_scale_keysClock = new util.Clock();
  text_top = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_top',
    text: 'Resize this image to match the size of a credit card\nUp arrow for taller\nDown arrow for shorter\nLeft arrow for narrower\nRight arrow for wider',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.5], draggable: false, height: 0.07,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_bottom = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_bottom',
    text: 'Press the space bar when done',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.6)], draggable: false, height: 0.07,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  ccimage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ccimage', units : 'pix', 
    image : 'bank-1300155_640.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [(x_size * x_scale), (y_size * y_scale)],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  // Initialize components for Routine "rectangle_keys"
  rectangle_keysClock = new util.Clock();
  rectangle_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'rectangle_text',
    text: 'This shape should be a 10 cm square.\nComponent size  (10*x_scale, 10*y_scale) set every repeat.\nPress space to continue.',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.6)], draggable: false, height: 0.07,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  polygon_keys = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_keys', units : 'pix', 
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color([1,1,1]), 
    fillColor: new util.Color([1,1,1]), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -1, 
    interpolate: true, 
  });
  
  key_resp_keys = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Instruction"
  InstructionClock = new util.Clock();
  text_inst = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_inst',
    text: 'Experimental Instruction\n\nWelcome to our reproduction experiment. Please focus during the experiment.\n\nIn this experiment, you will see a Gabor patch appear on the screen. You need to remember the DURATION of the Gabor patch. \nAfter it disappears,  you are asked to press the DOWN ARROW key as long as what you perceived. The key press will show a Gabor patch again, helping you compare the last duration. \n\nPress SPACE to continue...\n',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], draggable: false, height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  instr_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from code
  practice_count = 10
  //practice_count = 3 // piloting phase
  function generateSequence() {
      // Parameters
      const low = 600; // ms (minimum duration)
      const high = 1800; // ms (maximum duration)
      const step = 16.67; // ms (60Hz refresh rate)
      const n_trl = 100; // trials per block
      //const n_trl = 50; // piloting phase
  
      // ===== 1. Generate Random Walk (LOW stochasticity) =====
      let w = new Array(n_trl).fill(0);
      for (let i = 1; i < n_trl; i++) {
          // Smooth random walk: each step depends on the previous value
          w[i] = w[i-1] + (Math.random() * 2 - 1); // Small random step (-1 to +1)
      }
  
      // Normalize to mean=0, std=1
      const mean = w.reduce((a, b) => a + b, 0) / w.length;
      w = w.map(x => x - mean);
      const std = Math.sqrt(w.reduce((a, b) => a + b*b, 0) / w.length);
      w = w.map(x => x / std);
  
      // Scale to [low, high] range and round to nearest step (for 60Hz)
      const min = Math.min(...w);
      const max = Math.max(...w);
      w = w.map(x => 
          Math.round(((x - min) / (max - min) * (high - low) + low) / step) * step
      );
  
      // Low stochasticity block (w1 = random walk, in seconds)
      const w1 = w.map(x => parseFloat((x / 1000).toFixed(3))); // Round to 3 decimals
  
      // High stochasticity block (w2 = DEEPLY SHUFFLED w1)
      const w2 = [...w1];
      for (let i = w2.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1)); // Fisher-Yates shuffle
          [w2[i], w2[j]] = [w2[j], w2[i]];
      }
  
      // ===== 2. Assign Blocks (L-H-L or H-L-H) =====
      let durations, labels;
      if (Math.random() < 0.5) {
          // Low-High-Low condition
          durations = [...w1, ...w2, ...w1];
          labels = [
              ...Array(n_trl).fill('low'),
              ...Array(n_trl).fill('high'),
              ...Array(n_trl).fill('low')
          ];
      } else {
          // High-Low-High condition
          durations = [...w2, ...w1, ...w2];
          labels = [
              ...Array(n_trl).fill('high'),
              ...Array(n_trl).fill('low'),
              ...Array(n_trl).fill('high')
          ];
      }
  
      // ===== 3. Add Practice Trials =====
      const practice_options = [1.1, 1.2, 1.3];
      const practice_durations = Array(practice_count).fill(0)
          .map(() => parseFloat((practice_options[Math.floor(Math.random() * practice_options.length)]).toFixed(3))); // Round to 3 decimals
      const practice_labels = Array(practice_count).fill('practice');
  
      // Combine practice + main blocks
      durations = [...practice_durations, ...durations];
      labels = [...practice_labels, ...labels];
  
      // ===== 4. Create Trial List =====
      const trials = durations.map((duration, i) => ({
          trlno: i + 1,
          duration: duration,
          stochasticity: labels[i]
      }));
  
      console.log("Total trials:", trials.length);
  
      return trials;
  }
  subCond = generateSequence();
  console.log(subCond)
  console.log(subCond.length);
  // Initialize components for Routine "block"
  blockClock = new util.Clock();
  // Run 'Begin Experiment' code from code_2
  Block_text = "";
  showBlockText = false;
  
  // kb = new core.Keyboard({ psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true });
  blockText = new visual.TextStim({
    win: psychoJS.window,
    name: 'blockText',
    text: '',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], draggable: false, height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Encoding"
  EncodingClock = new util.Clock();
  stimulus_grating = new visual.GratingStim({
    win : psychoJS.window,
    name : 'stimulus_grating', units : 'norm', 
    tex : undefined, mask : 'gauss',
    ori : 1.0, 
    pos : [0, 0],
    draggable: false,
    anchor : 'center',
    sf : 5.0, phase : 0.0,
    size : [(0.005 * x_scale), (0.014 * y_scale)],
    color : new util.Color([1,1,1]), opacity : undefined,
    contrast : 0.4, blendmode : 'avg',
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  fixation = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation', units : 'height', 
    vertices: 'cross', size:[(0.0004 * x_scale), (0.0004 * x_scale)],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -2, 
    interpolate: true, 
  });
  
  // Initialize components for Routine "cue_to_reproduce"
  cue_to_reproduceClock = new util.Clock();
  rep_cue = new visual.Polygon({
    win: psychoJS.window, name: 'rep_cue', units : 'height', 
    edges: 100, size:[(0.0004 * x_scale), (0.0004 * x_scale)],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color([0.1294, 0.8667, 0.1294]), 
    fillColor: new util.Color([0.1294, 0.8667, 0.1294]), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: 0, 
    interpolate: true, 
  });
  
  // Initialize components for Routine "Reproduction"
  ReproductionClock = new util.Clock();
  gabor = new visual.GratingStim({
    win : psychoJS.window,
    name : 'gabor', units : 'norm', 
    tex : undefined, mask : 'gauss',
    ori : 1.0, 
    pos : [0, 0],
    draggable: false,
    anchor : 'center',
    sf : 5.0, phase : 0.0,
    size : [(0.005 * x_scale), (0.014 * y_scale)],
    color : new util.Color([1,1,1]), opacity : undefined,
    contrast : 0.4, blendmode : 'avg',
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Run 'Begin Experiment' code from code_reproduction
  // kb = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  showFeedback = false;
  feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text',
    text: '',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], draggable: false, height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "iti"
  itiClock = new util.Clock();
  iti_blank = new visual.TextStim({
    win: psychoJS.window,
    name: 'iti_blank',
    text: '',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], draggable: false, height: 0.5,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Goodbye"
  GoodbyeClock = new util.Clock();
  goodbye_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'goodbye_text',
    text: 'The whole experiment is completed! \n\nMany thanks for your participation!\n\nPress SPACE to exit...',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], draggable: false, height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  goodbye_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var scale_setupMaxDurationReached;
var scale_setupMaxDuration;
var scale_setupComponents;
function scale_setupRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'scale_setup' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    scale_setupClock.reset();
    routineTimer.reset();
    scale_setupMaxDurationReached = false;
    // update component parameters for each repeat
    scale_setupMaxDuration = null
    // keep track of which components have finished
    scale_setupComponents = [];
    
    for (const thisComponent of scale_setupComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function scale_setupRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'scale_setup' ---
    // get current time
    t = scale_setupClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of scale_setupComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function scale_setupRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'scale_setup' ---
    for (const thisComponent of scale_setupComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "scale_setup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var key_scale;
function key_scaleLoopBegin(key_scaleLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    key_scale = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'key_scale'
    });
    psychoJS.experiment.addLoop(key_scale); // add the loop to the experiment
    currentLoop = key_scale;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisKey_scale of key_scale) {
      snapshot = key_scale.getSnapshot();
      key_scaleLoopScheduler.add(importConditions(snapshot));
      key_scaleLoopScheduler.add(screen_scale_keysRoutineBegin(snapshot));
      key_scaleLoopScheduler.add(screen_scale_keysRoutineEachFrame());
      key_scaleLoopScheduler.add(screen_scale_keysRoutineEnd(snapshot));
      key_scaleLoopScheduler.add(rectangle_keysRoutineBegin(snapshot));
      key_scaleLoopScheduler.add(rectangle_keysRoutineEachFrame());
      key_scaleLoopScheduler.add(rectangle_keysRoutineEnd(snapshot));
      key_scaleLoopScheduler.add(key_scaleLoopEndIteration(key_scaleLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function key_scaleLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(key_scale);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function key_scaleLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: subCond,
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(blockRoutineBegin(snapshot));
      trialsLoopScheduler.add(blockRoutineEachFrame());
      trialsLoopScheduler.add(blockRoutineEnd(snapshot));
      trialsLoopScheduler.add(EncodingRoutineBegin(snapshot));
      trialsLoopScheduler.add(EncodingRoutineEachFrame());
      trialsLoopScheduler.add(EncodingRoutineEnd(snapshot));
      trialsLoopScheduler.add(cue_to_reproduceRoutineBegin(snapshot));
      trialsLoopScheduler.add(cue_to_reproduceRoutineEachFrame());
      trialsLoopScheduler.add(cue_to_reproduceRoutineEnd(snapshot));
      trialsLoopScheduler.add(ReproductionRoutineBegin(snapshot));
      trialsLoopScheduler.add(ReproductionRoutineEachFrame());
      trialsLoopScheduler.add(ReproductionRoutineEnd(snapshot));
      trialsLoopScheduler.add(feedbackRoutineBegin(snapshot));
      trialsLoopScheduler.add(feedbackRoutineEachFrame());
      trialsLoopScheduler.add(feedbackRoutineEnd(snapshot));
      trialsLoopScheduler.add(itiRoutineBegin(snapshot));
      trialsLoopScheduler.add(itiRoutineEachFrame());
      trialsLoopScheduler.add(itiRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var screen_scale_keysMaxDurationReached;
var screen_scale_keysMaxDuration;
var screen_scale_keysComponents;
function screen_scale_keysRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'screen_scale_keys' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    screen_scale_keysClock.reset();
    routineTimer.reset();
    screen_scale_keysMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from scale_keys_code
    console.log("key start");
    psychoJS.eventManager.clearEvents();
    
    screen_scale_keysMaxDuration = null
    // keep track of which components have finished
    screen_scale_keysComponents = [];
    screen_scale_keysComponents.push(text_top);
    screen_scale_keysComponents.push(text_bottom);
    screen_scale_keysComponents.push(ccimage);
    
    for (const thisComponent of screen_scale_keysComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var _pj;
var keys;
var dscale;
function screen_scale_keysRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'screen_scale_keys' ---
    // get current time
    t = screen_scale_keysClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from scale_keys_code
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = psychoJS.eventManager.getKeys();
    if (keys.length) {
        if (((t - oldt) < 0.5)) {
            dscale = (5 * dbase);
            oldt = t;
        } else {
            dscale = dbase;
            oldt = t;
        }
        if ((_pj.in_es6("space", keys) && (t > 1))) {
            continueRoutine = false;
        } else {
            if (_pj.in_es6("up", keys)) {
                y_scale = (util.round(((y_scale + dscale) * 10000)) / 10000);
            } else {
                if (_pj.in_es6("down", keys)) {
                    y_scale = (util.round(((y_scale - dscale) * 10000)) / 10000);
                } else {
                    if (_pj.in_es6("left", keys)) {
                        x_scale = (util.round(((x_scale - dscale) * 10000)) / 10000);
                    } else {
                        if (_pj.in_es6("right", keys)) {
                            x_scale = (util.round(((x_scale + dscale) * 10000)) / 10000);
                        }
                    }
                }
            }
        }
        screen_height = (util.round(((vsize * 10) / y_scale)) / 10);
        text_bottom.text = (((((((("X Scale = " + x_scale.toString()) + unittext) + " per cm, Y Scale = ") + y_scale.toString()) + unittext) + " per cm\nScreen height = ") + screen_height.toString()) + " cm\n\nPress the space bar when done");
        ccimage.size = [(x_size * x_scale), (y_size * y_scale)];
    }
    
    
    // *text_top* updates
    if (t >= 0.0 && text_top.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_top.tStart = t;  // (not accounting for frame time here)
      text_top.frameNStart = frameN;  // exact frame index
      
      text_top.setAutoDraw(true);
    }
    
    
    // *text_bottom* updates
    if (t >= 0.0 && text_bottom.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_bottom.tStart = t;  // (not accounting for frame time here)
      text_bottom.frameNStart = frameN;  // exact frame index
      
      text_bottom.setAutoDraw(true);
    }
    
    
    // *ccimage* updates
    if (t >= 0.0 && ccimage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ccimage.tStart = t;  // (not accounting for frame time here)
      ccimage.frameNStart = frameN;  // exact frame index
      
      ccimage.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of screen_scale_keysComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function screen_scale_keysRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'screen_scale_keys' ---
    for (const thisComponent of screen_scale_keysComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from scale_keys_code
    psychoJS.experiment.addData("X Scale", x_scale);
    psychoJS.experiment.addData("Y Scale", y_scale);
    
    // the Routine "screen_scale_keys" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var rectangle_keysMaxDurationReached;
var _key_resp_keys_allKeys;
var rectangle_keysMaxDuration;
var rectangle_keysComponents;
function rectangle_keysRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'rectangle_keys' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    rectangle_keysClock.reset();
    routineTimer.reset();
    rectangle_keysMaxDurationReached = false;
    // update component parameters for each repeat
    polygon_keys.setSize([(10 * x_scale), (10 * y_scale)]);
    key_resp_keys.keys = undefined;
    key_resp_keys.rt = undefined;
    _key_resp_keys_allKeys = [];
    rectangle_keysMaxDuration = null
    // keep track of which components have finished
    rectangle_keysComponents = [];
    rectangle_keysComponents.push(rectangle_text);
    rectangle_keysComponents.push(polygon_keys);
    rectangle_keysComponents.push(key_resp_keys);
    
    for (const thisComponent of rectangle_keysComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function rectangle_keysRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'rectangle_keys' ---
    // get current time
    t = rectangle_keysClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rectangle_text* updates
    if (t >= 0.0 && rectangle_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rectangle_text.tStart = t;  // (not accounting for frame time here)
      rectangle_text.frameNStart = frameN;  // exact frame index
      
      rectangle_text.setAutoDraw(true);
    }
    
    
    // *polygon_keys* updates
    if (t >= 0.0 && polygon_keys.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_keys.tStart = t;  // (not accounting for frame time here)
      polygon_keys.frameNStart = frameN;  // exact frame index
      
      polygon_keys.setAutoDraw(true);
    }
    
    
    // *key_resp_keys* updates
    if (t >= 0.0 && key_resp_keys.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_keys.tStart = t;  // (not accounting for frame time here)
      key_resp_keys.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_keys.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_keys.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_keys.clearEvents(); });
    }
    
    if (key_resp_keys.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_keys.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_keys_allKeys = _key_resp_keys_allKeys.concat(theseKeys);
      if (_key_resp_keys_allKeys.length > 0) {
        key_resp_keys.keys = _key_resp_keys_allKeys[_key_resp_keys_allKeys.length - 1].name;  // just the last key pressed
        key_resp_keys.rt = _key_resp_keys_allKeys[_key_resp_keys_allKeys.length - 1].rt;
        key_resp_keys.duration = _key_resp_keys_allKeys[_key_resp_keys_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of rectangle_keysComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function rectangle_keysRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'rectangle_keys' ---
    for (const thisComponent of rectangle_keysComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_keys.corr, level);
    }
    psychoJS.experiment.addData('key_resp_keys.keys', key_resp_keys.keys);
    if (typeof key_resp_keys.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_keys.rt', key_resp_keys.rt);
        psychoJS.experiment.addData('key_resp_keys.duration', key_resp_keys.duration);
        routineTimer.reset();
        }
    
    key_resp_keys.stop();
    // the Routine "rectangle_keys" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var InstructionMaxDurationReached;
var _instr_key_allKeys;
var InstructionMaxDuration;
var InstructionComponents;
function InstructionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instruction' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    InstructionClock.reset();
    routineTimer.reset();
    InstructionMaxDurationReached = false;
    // update component parameters for each repeat
    instr_key.keys = undefined;
    instr_key.rt = undefined;
    _instr_key_allKeys = [];
    InstructionMaxDuration = null
    // keep track of which components have finished
    InstructionComponents = [];
    InstructionComponents.push(text_inst);
    InstructionComponents.push(instr_key);
    
    for (const thisComponent of InstructionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function InstructionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instruction' ---
    // get current time
    t = InstructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_inst* updates
    if (t >= 0.0 && text_inst.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_inst.tStart = t;  // (not accounting for frame time here)
      text_inst.frameNStart = frameN;  // exact frame index
      
      text_inst.setAutoDraw(true);
    }
    
    
    // *instr_key* updates
    if (t >= 0.0 && instr_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_key.tStart = t;  // (not accounting for frame time here)
      instr_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instr_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instr_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instr_key.clearEvents(); });
    }
    
    if (instr_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = instr_key.getKeys({keyList: ['space'], waitRelease: false});
      _instr_key_allKeys = _instr_key_allKeys.concat(theseKeys);
      if (_instr_key_allKeys.length > 0) {
        instr_key.keys = _instr_key_allKeys[_instr_key_allKeys.length - 1].name;  // just the last key pressed
        instr_key.rt = _instr_key_allKeys[_instr_key_allKeys.length - 1].rt;
        instr_key.duration = _instr_key_allKeys[_instr_key_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstructionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instruction' ---
    for (const thisComponent of InstructionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    instr_key.stop();
    // the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var blockMaxDurationReached;
var _key_resp_allKeys;
var blockMaxDuration;
var blockComponents;
function blockRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'block' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    blockClock.reset();
    routineTimer.reset();
    blockMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_2
    continueRoutine = false;
    console.log(stochasticity);
    let trialIndex = trials.thisTrialN;  // 0-based trial number
    
    if (trialIndex === 0) {
        Block_text = `Practice will start.\n\nPlease press SPACE to continue.`;
        continueRoutine = true;
    }
    //else if (trialIndex === 3) {
    else if (trialIndex === 10) {
        Block_text = `Formal Experiment will start now. \n\nBlock 1 of 3.\n\nPlease press SPACE to continue.`;
        skipRoutine = true
        continueRoutine = true;
    }
    
    //else if (trialIndex === 6) {
    else if (trialIndex === 110) {
        Block_text = `Block 1/3 complete.\nYou did a great job, please take a rest.\n\n\nPress SPACE to continue.`;
    }
    //else if (trialIndex === 9) {
    else if (trialIndex === 210) {
        Block_text = `Block 2/3 complete.\nYou did a great job, please take a rest.\n\nPress SPACE to continue.`;
        continueRoutine = true;
    }
    
    if (continueRoutine) {
        blockText.setText(Block_text);
    }
    
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    blockMaxDuration = null
    // keep track of which components have finished
    blockComponents = [];
    blockComponents.push(blockText);
    blockComponents.push(key_resp);
    
    for (const thisComponent of blockComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function blockRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'block' ---
    // get current time
    t = blockClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (blockText.status === PsychoJS.Status.STARTED){ // only update if being drawn
      blockText.setText(Block_text, false);
    }
    
    // *blockText* updates
    if (t >= 0 && blockText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blockText.tStart = t;  // (not accounting for frame time here)
      blockText.frameNStart = frameN;  // exact frame index
      
      blockText.setAutoDraw(true);
    }
    
    
    // *key_resp* updates
    if (t >= 0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of blockComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function blockRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'block' ---
    for (const thisComponent of blockComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp.stop();
    // the Routine "block" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var EncodingMaxDurationReached;
var orientation;
var EncodingMaxDuration;
var EncodingComponents;
function EncodingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Encoding' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    EncodingClock.reset();
    routineTimer.reset();
    EncodingMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_encoding
    orientation = util.randint(1, 180);
    
    EncodingMaxDuration = null
    // keep track of which components have finished
    EncodingComponents = [];
    EncodingComponents.push(stimulus_grating);
    EncodingComponents.push(fixation);
    
    for (const thisComponent of EncodingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function EncodingRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Encoding' ---
    // get current time
    t = EncodingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (stimulus_grating.status === PsychoJS.Status.STARTED){ // only update if being drawn
      stimulus_grating.setOri(orientation, false);
    }
    
    // *stimulus_grating* updates
    if (t >= 0.5 && stimulus_grating.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimulus_grating.tStart = t;  // (not accounting for frame time here)
      stimulus_grating.frameNStart = frameN;  // exact frame index
      
      stimulus_grating.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + duration - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (stimulus_grating.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      stimulus_grating.setAutoDraw(false);
    }
    
    
    // *fixation* updates
    if (t >= 0.0 && fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation.tStart = t;  // (not accounting for frame time here)
      fixation.frameNStart = frameN;  // exact frame index
      
      fixation.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EncodingComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EncodingRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Encoding' ---
    for (const thisComponent of EncodingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "Encoding" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var cue_to_reproduceMaxDurationReached;
var cue_to_reproduceMaxDuration;
var cue_to_reproduceComponents;
function cue_to_reproduceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'cue_to_reproduce' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    cue_to_reproduceClock.reset(routineTimer.getTime());
    routineTimer.add(0.600000);
    cue_to_reproduceMaxDurationReached = false;
    // update component parameters for each repeat
    cue_to_reproduceMaxDuration = null
    // keep track of which components have finished
    cue_to_reproduceComponents = [];
    cue_to_reproduceComponents.push(rep_cue);
    
    for (const thisComponent of cue_to_reproduceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function cue_to_reproduceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'cue_to_reproduce' ---
    // get current time
    t = cue_to_reproduceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rep_cue* updates
    if (t >= 0.3 && rep_cue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rep_cue.tStart = t;  // (not accounting for frame time here)
      rep_cue.frameNStart = frameN;  // exact frame index
      
      rep_cue.setAutoDraw(true);
    }
    
    frameRemains = 0.3 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (rep_cue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rep_cue.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of cue_to_reproduceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function cue_to_reproduceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'cue_to_reproduce' ---
    for (const thisComponent of cue_to_reproduceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if (cue_to_reproduceMaxDurationReached) {
        cue_to_reproduceClock.add(cue_to_reproduceMaxDuration);
    } else {
        cue_to_reproduceClock.add(0.600000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ReproductionMaxDurationReached;
var keyPressed;
var keyReleased;
var repDuration;
var keyOnset;
var keyOffset;
var kb;
var ReproductionMaxDuration;
var ReproductionComponents;
function ReproductionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Reproduction' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    ReproductionClock.reset();
    routineTimer.reset();
    ReproductionMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_reproduction
    /*kb.start();
    keyPressed = false;
    keyReleased = false;
    keyOnset = null;
    repDuration = null;
    gabor.setAutoDraw(false); */
    
    keyPressed = false;
    keyReleased = false;
    repDuration = 0;
    keyOnset = 0;
    keyOffset = 0;
    
    kb = new core.Keyboard({ psychoJS: psychoJS, clock: new util.Clock(), waitForStart: false });
    kb.start();
    
    
    ReproductionMaxDuration = null
    // keep track of which components have finished
    ReproductionComponents = [];
    ReproductionComponents.push(gabor);
    
    for (const thisComponent of ReproductionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ReproductionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Reproduction' ---
    // get current time
    t = ReproductionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (gabor.status === PsychoJS.Status.STARTED){ // only update if being drawn
      gabor.setOri(orientation, false);
    }
    
    // *gabor* updates
    if ((0) && gabor.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      gabor.tStart = t;  // (not accounting for frame time here)
      gabor.frameNStart = frameN;  // exact frame index
      
      gabor.setAutoDraw(true);
    }
    
    // Check for key events
    let keyEvents = kb.getEvents();
    let keyName, status;
    
    for (let i = 0; i < keyEvents.length; i++) {
        let event = keyEvents[i];
        keyName = event.pigletKey;  // e.g., 'ArrowDown'
        status = event.status;      // Symbol.for('KEY_DOWN') or Symbol.for('KEY_UP')
        console.log(keyName);
    
        if (keyName === 'down') {
            if (status === Symbol.for('KEY_DOWN')) {
                // Only store the first press time
                if (!keyPressed) {
                    keyPressed = true;
                    keyOnset = globalClock.getTime();
                    gabor.setAutoDraw(true);
                    console.log("Key DOWN at:", keyOnset);
                }
            } 
            else if (status === Symbol.for('KEY_UP') && keyPressed) {
                keyOffset = globalClock.getTime();
                repDuration = keyOffset - keyOnset;
                gabor.setAutoDraw(false);
    
                console.log("Key UP at:", keyOffset);
                console.log("Duration:", repDuration);
                //console.log(repDuration, "=", keyOffset, "-", keyOnset);
    
                // Save data and end routine
                psychoJS.experiment.addData('press_time', keyOnset);
                psychoJS.experiment.addData('duration', repDuration);
                continueRoutine = false;
            }
        }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ReproductionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var error_ratio;
var skipRoutine;
function ReproductionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Reproduction' ---
    for (const thisComponent of ReproductionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from code_reproduction
    psychoJS.experiment.addData("orientation", orientation);
    psychoJS.experiment.addData("rpr_onset", keyOnset);
    psychoJS.experiment.addData("rpr_duration", repDuration);
    if (stochasticity === 'practice') {
        error_ratio = Math.abs((repDuration / duration) - 1);
        skipRoutine = (trlno > 10) || (error_ratio <= 0.4);
        }
    
    // the Routine "Reproduction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedbackMaxDurationReached;
var fb_text;
var _key_resp_2_allKeys;
var maxDurationReached;
var feedbackMaxDuration;
var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedbackClock.reset();
    routineTimer.reset();
    feedbackMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from feedback_code
    showFeedback = false;  // default: don't show
    
    if (stochasticity === 'practice') {
            error_ratio = Math.abs((repDuration / duration) - 1);
        
            if (error_ratio > 0.4) {
                fb_text = `Your key pressed duration deviated too far!\n\n\npress SPACE to continue`;
                showFeedback = true;
            } else {
                fb_text = "";
            }
        } else {
            fb_text = "";  // formal trials shouldn't show feedback
        }
    
    
    
    feedback_text.setText(fb_text);
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // skip this Routine if its 'Skip if' condition is True
    continueRoutine = continueRoutine && !(skipRoutine);
    maxDurationReached = false
    feedbackMaxDuration = null
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(feedback_text);
    feedbackComponents.push(key_resp_2);
    
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback' ---
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text* updates
    if (t >= 0.0 && feedback_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text.tStart = t;  // (not accounting for frame time here)
      feedback_text.frameNStart = frameN;  // exact frame index
      
      feedback_text.setAutoDraw(true);
    }
    
    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }
    
    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        key_resp_2.duration = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback' ---
    for (const thisComponent of feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        psychoJS.experiment.addData('key_resp_2.duration', key_resp_2.duration);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var itiMaxDurationReached;
var itiMaxDuration;
var itiComponents;
function itiRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'iti' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    itiClock.reset(routineTimer.getTime());
    routineTimer.add(0.700000);
    itiMaxDurationReached = false;
    // update component parameters for each repeat
    itiMaxDuration = null
    // keep track of which components have finished
    itiComponents = [];
    itiComponents.push(iti_blank);
    
    for (const thisComponent of itiComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function itiRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'iti' ---
    // get current time
    t = itiClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *iti_blank* updates
    if (t >= 0.0 && iti_blank.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      iti_blank.tStart = t;  // (not accounting for frame time here)
      iti_blank.frameNStart = frameN;  // exact frame index
      
      iti_blank.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.7 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (iti_blank.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      iti_blank.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of itiComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function itiRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'iti' ---
    for (const thisComponent of itiComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if (itiMaxDurationReached) {
        itiClock.add(itiMaxDuration);
    } else {
        itiClock.add(0.700000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var GoodbyeMaxDurationReached;
var _goodbye_key_allKeys;
var GoodbyeMaxDuration;
var GoodbyeComponents;
function GoodbyeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Goodbye' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    GoodbyeClock.reset();
    routineTimer.reset();
    GoodbyeMaxDurationReached = false;
    // update component parameters for each repeat
    goodbye_key.keys = undefined;
    goodbye_key.rt = undefined;
    _goodbye_key_allKeys = [];
    // Disable downloading results to browser
    psychoJS._saveResults = 0;
    
    // Generate filename for results
    let filename = psychoJS._experiment._experimentName + '_' + psychoJS._experiment._datetime + '.csv';
    
    // Extract data object from experiment
    let dataObj = psychoJS._experiment._trialsData;
    
    // Convert data object to CSV format
    let data = [Object.keys(dataObj[0])]
        .concat(dataObj.map(it => Object.values(it).toString()))
        .join('\n');
    
    // Send data to OSF via DataPipe
    console.log('Saving data...');
    
    fetch('https://pipe.jspsych.org/api/data/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': '*/*'
        },
        body: JSON.stringify({
            experimentID: 'ALvQXbIMCM0V', // ★ Replace with your Datapipe experiment ID ★
            filename: filename,
            data: data,
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        quitPsychoJS();
    });
    GoodbyeMaxDuration = null
    // keep track of which components have finished
    GoodbyeComponents = [];
    GoodbyeComponents.push(goodbye_text);
    GoodbyeComponents.push(goodbye_key);
    
    for (const thisComponent of GoodbyeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function GoodbyeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Goodbye' ---
    // get current time
    t = GoodbyeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *goodbye_text* updates
    if (t >= 0.0 && goodbye_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      goodbye_text.tStart = t;  // (not accounting for frame time here)
      goodbye_text.frameNStart = frameN;  // exact frame index
      
      goodbye_text.setAutoDraw(true);
    }
    
    
    // *goodbye_key* updates
    if (t >= 0.0 && goodbye_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      goodbye_key.tStart = t;  // (not accounting for frame time here)
      goodbye_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { goodbye_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { goodbye_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { goodbye_key.clearEvents(); });
    }
    
    if (goodbye_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = goodbye_key.getKeys({keyList: ['space'], waitRelease: false});
      _goodbye_key_allKeys = _goodbye_key_allKeys.concat(theseKeys);
      if (_goodbye_key_allKeys.length > 0) {
        goodbye_key.keys = _goodbye_key_allKeys[_goodbye_key_allKeys.length - 1].name;  // just the last key pressed
        goodbye_key.rt = _goodbye_key_allKeys[_goodbye_key_allKeys.length - 1].rt;
        goodbye_key.duration = _goodbye_key_allKeys[_goodbye_key_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of GoodbyeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function GoodbyeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Goodbye' ---
    for (const thisComponent of GoodbyeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(goodbye_key.corr, level);
    }
    psychoJS.experiment.addData('goodbye_key.keys', goodbye_key.keys);
    if (typeof goodbye_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('goodbye_key.rt', goodbye_key.rt);
        psychoJS.experiment.addData('goodbye_key.duration', goodbye_key.duration);
        routineTimer.reset();
        }
    
    goodbye_key.stop();
    // the Routine "Goodbye" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
