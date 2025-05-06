#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on May 06, 2025, at 13:39
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2024')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from feedback_code
fb_text  = ''
# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'vol_reproduction'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):04.0f}",
    'prolificID': '',
    'gender (M/F)': '',
    'age': '',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1920, 1080]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s' % (expName, expInfo['participant'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\ayzac\\Desktop\\bachelor thesis\\vtr_online\\vol_reproduction_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('', )
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('data')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='pix',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'pix'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # --- Setup iohub hdf5 datastore ---
    ioSession = str(expInfo.get('session', '1'))
    ioDataStoreConfig = {
        'experiment_code': 'vol_reproduction',
        'session_code': ioSession,
        'datastore_name': thisExp.dataFileName,
    }
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    if deviceManager.getDevice('key_resp_keys') is None:
        # initialise key_resp_keys
        key_resp_keys = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_keys',
        )
    if deviceManager.getDevice('instr_key') is None:
        # initialise instr_key
        instr_key = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='instr_key',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('goodbye_key') is None:
        # initialise goodbye_key
        goodbye_key = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='goodbye_key',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "scale_setup" ---
    # Run 'Begin Experiment' code from scale_code
    oldt=0
    x_size=8.560
    y_size=5.398
    screen_height=0
    
    if win.units=='norm':
        x_scale=.05
        y_scale=.1
        dbase = .0001
        unittext=' norm units'
        vsize=2
    elif win.units=='pix':
        x_scale=60
        y_scale=40
        dbase = .1
        unittext=' pixels'
        vsize=win.size[1]
    else:
        x_scale=.05
        y_scale=.05
        dbase = .0001
        unittext=' height units'
        vsize=1
    
    # --- Initialize components for Routine "screen_scale_keys" ---
    text_top = visual.TextStim(win=win, name='text_top',
        text='Resize this image to match the size of a credit card\nUp arrow for taller\nDown arrow for shorter\nLeft arrow for narrower\nRight arrow for wider',
        font='Arial',
        units='norm', pos=(0, .7), draggable=False, height=0.1, wrapWidth=1.5, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    text_bottom = visual.TextStim(win=win, name='text_bottom',
        text='Press the space bar when done',
        font='Arial',
        units='norm', pos=(0, -.6), draggable=False, height=0.1, wrapWidth=1.5, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    ccimage = visual.ImageStim(
        win=win,
        name='ccimage', units='pix', 
        image='bank-1300155_640.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(x_size*x_scale, y_size*y_scale),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "rectangle_keys" ---
    rectangle_text = visual.TextStim(win=win, name='rectangle_text',
        text='This shape should be a 10 cm square.\nComponent size  (10*x_scale, 10*y_scale) set every repeat.\nPress space to continue.',
        font='Arial',
        units='norm', pos=(0, -.8), draggable=False, height=0.1, wrapWidth=1.5, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    polygon_keys = visual.Rect(
        win=win, name='polygon_keys',units='pix', 
        width=[1.0, 1.0][0], height=[1.0, 1.0][1],
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=None, depth=-1.0, interpolate=True)
    key_resp_keys = keyboard.Keyboard(deviceName='key_resp_keys')
    
    # --- Initialize components for Routine "Instruction" ---
    text_inst = visual.TextStim(win=win, name='text_inst',
        text="Experimental Instruction\n\nWelcome to our reproduction experiment. In this experiment, you will see a Gabor patch appears on the screen. You need to remember the DURATION of the Gabor patch. After it disappears, you are asked to press the 'Down' Arrow key as long as what you perceived. The key press will show a Gabor patch again, helping you compare the last duration. \n\nPress SPACE to start ...\n",
        font='Arial',
        units='norm', pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    instr_key = keyboard.Keyboard(deviceName='instr_key')
    # Run 'Begin Experiment' code from code
    import numpy as np
    import pandas as pd
    
    #generate sequence
    low = 600 #ms
    high = 1800 #ms
    step = 16.67 #ms for 60Hz refresh rate
    #n_trl = 100
    n_trl = 3 # piloting phase
    
    w = np.cumsum(np.random.randn(n_trl)) #random walk
    w = (w - w.mean()) / w.std() #normalization
    w = (w - w.min()) / (w.max() - w.min()) * (high - low) + low # to low-high range
    w = np.round(w / step) * step #round to the refresh time
    
    w1 = np.round(w) #random walk round - low
    w2 = np.random.permutation(w1) #shuffled - high
    
        
    # choose block order
    if np.random.rand() < 0.5:
        durations = np.concatenate([w1, w2])/1000.0
        labels    = ['low'] * n_trl + ['high'] * n_trl
    else:
        durations = np.concatenate([w2, w1])/1000.0
        labels    = ['high'] * n_trl + ['low'] * n_trl
    
    # Practice trials
    #practice_count = 10
    practice_count = 3 # piloting phase
    practice_options = [1.1, 1.2, 1.3]
    practice_durations = np.random.choice(practice_options,
            size=practice_count,replace=True).tolist()
    practice_labels = ['practice'] * practice_count
    
    # Combine practice + blocks
    durations = practice_durations + durations.tolist()
    labels = practice_labels + labels
    
    df = pd.DataFrame({
        'trlno':         np.arange(1, 2*n_trl + 1 + practice_count),
        'duration':   durations, # in sec
        'stochasticity': labels
    })
    # save to subfolder condition
    subCond = 'sub_seqs/' + expInfo['participant'] + '.csv'
    df.to_csv(subCond, index = False)
    
    # --- Initialize components for Routine "block" ---
    text = visual.TextStim(win=win, name='text',
        text='',
        font='Arial',
        units='norm', pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    # Run 'Begin Experiment' code from code_2
    Block_text=''
    
    
    # --- Initialize components for Routine "Encoding" ---
    stimulus_grating = visual.GratingStim(
        win=win, name='stimulus_grating',units='norm', 
        tex='sin', mask='gauss', anchor='center',
        ori=1.0, pos=(0, 0), draggable=False, size=(0.007*x_scale, 0.015*y_scale), sf=5.0, phase=0.0,
        color=[1,1,1], colorSpace='rgb',
        opacity=None, contrast=0.4, blendmode='avg',
        texRes=128.0, interpolate=True, depth=0.0)
    fixation = visual.ShapeStim(
        win=win, name='fixation', vertices='cross',units='height', 
        size=(0.001*x_scale, 0.001*x_scale),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    
    # --- Initialize components for Routine "cue_to_reproduce" ---
    rep_cue = visual.ShapeStim(
        win=win, name='rep_cue',units='height', 
        size=(0.0007*x_scale, 0.0007*x_scale), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[0.1294, 0.8667, 0.1294], fillColor=[0.1294, 0.8667, 0.1294],
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "Reproduction" ---
    gabor = visual.GratingStim(
        win=win, name='gabor',units='norm', 
        tex='sin', mask='gauss', anchor='center',
        ori=1.0, pos=(0, 0), draggable=False, size=(0.007*x_scale, 0.015*y_scale), sf=5.0, phase=0.0,
        color=[1,1,1], colorSpace='rgb',
        opacity=None, contrast=0.4, blendmode='avg',
        texRes=128.0, interpolate=True, depth=0.0)
    # Run 'Begin Experiment' code from code_reproduction
    from psychopy.hardware.keyboard import Keyboard
    kb = Keyboard()
    
    
    # --- Initialize components for Routine "feedback" ---
    feedback_text = visual.TextStim(win=win, name='feedback_text',
        text='',
        font='Arial',
        units='norm', pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "iti" ---
    iti_blank = visual.TextStim(win=win, name='iti_blank',
        text=None,
        font='Arial',
        units='deg', pos=(0, 0), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Goodbye" ---
    goodbye_text = visual.TextStim(win=win, name='goodbye_text',
        text='The whole experiment is completed! \n\nMany thanks for your participation!\n\nPress SPACE to exit...',
        font='Arial',
        units='norm', pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    goodbye_key = keyboard.Keyboard(deviceName='goodbye_key')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "scale_setup" ---
    # create an object to store info about Routine scale_setup
    scale_setup = data.Routine(
        name='scale_setup',
        components=[],
    )
    scale_setup.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for scale_setup
    scale_setup.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    scale_setup.tStart = globalClock.getTime(format='float')
    scale_setup.status = STARTED
    scale_setup.maxDuration = None
    # keep track of which components have finished
    scale_setupComponents = scale_setup.components
    for thisComponent in scale_setup.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "scale_setup" ---
    scale_setup.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            scale_setup.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in scale_setup.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "scale_setup" ---
    for thisComponent in scale_setup.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for scale_setup
    scale_setup.tStop = globalClock.getTime(format='float')
    scale_setup.tStopRefresh = tThisFlipGlobal
    thisExp.nextEntry()
    # the Routine "scale_setup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    key_scale = data.TrialHandler2(
        name='key_scale',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(key_scale)  # add the loop to the experiment
    thisKey_scale = key_scale.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisKey_scale.rgb)
    if thisKey_scale != None:
        for paramName in thisKey_scale:
            globals()[paramName] = thisKey_scale[paramName]
    
    for thisKey_scale in key_scale:
        currentLoop = key_scale
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisKey_scale.rgb)
        if thisKey_scale != None:
            for paramName in thisKey_scale:
                globals()[paramName] = thisKey_scale[paramName]
        
        # --- Prepare to start Routine "screen_scale_keys" ---
        # create an object to store info about Routine screen_scale_keys
        screen_scale_keys = data.Routine(
            name='screen_scale_keys',
            components=[text_top, text_bottom, ccimage],
        )
        screen_scale_keys.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from scale_keys_code
        print('key start')
        event.clearEvents()
        # store start times for screen_scale_keys
        screen_scale_keys.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        screen_scale_keys.tStart = globalClock.getTime(format='float')
        screen_scale_keys.status = STARTED
        screen_scale_keys.maxDuration = None
        # keep track of which components have finished
        screen_scale_keysComponents = screen_scale_keys.components
        for thisComponent in screen_scale_keys.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "screen_scale_keys" ---
        # if trial has changed, end Routine now
        if isinstance(key_scale, data.TrialHandler2) and thisKey_scale.thisN != key_scale.thisTrial.thisN:
            continueRoutine = False
        screen_scale_keys.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from scale_keys_code
            keys=event.getKeys()
            
            if len(keys):
                if t-oldt<.5:
                    dscale=5*dbase
                    oldt=t
                else:
                    dscale=dbase
                    oldt=t
                if 'space' in keys and t > 1:
                    continueRoutine=False
                elif 'up' in keys:
                    y_scale=round((y_scale+dscale)*10000)/10000
                elif 'down' in keys:
                    y_scale=round((y_scale-dscale)*10000)/10000
                elif 'left' in keys:
                    x_scale=round((x_scale-dscale)*10000)/10000
                elif 'right' in keys:
                    x_scale=round((x_scale+dscale)*10000)/10000
                screen_height=round(vsize*10/y_scale)/10
                text_bottom.text='X Scale = '+str(x_scale)+unittext+' per cm, Y Scale = '+str(y_scale)+unittext+' per cm\nScreen height = '+str(screen_height)+' cm\n\nPress the space bar when done'
                ccimage.size=[x_size*x_scale, y_size*y_scale]
                
            
            # *text_top* updates
            
            # if text_top is starting this frame...
            if text_top.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_top.frameNStart = frameN  # exact frame index
                text_top.tStart = t  # local t and not account for scr refresh
                text_top.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_top, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_top.status = STARTED
                text_top.setAutoDraw(True)
            
            # if text_top is active this frame...
            if text_top.status == STARTED:
                # update params
                pass
            
            # *text_bottom* updates
            
            # if text_bottom is starting this frame...
            if text_bottom.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_bottom.frameNStart = frameN  # exact frame index
                text_bottom.tStart = t  # local t and not account for scr refresh
                text_bottom.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_bottom, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_bottom.status = STARTED
                text_bottom.setAutoDraw(True)
            
            # if text_bottom is active this frame...
            if text_bottom.status == STARTED:
                # update params
                pass
            
            # *ccimage* updates
            
            # if ccimage is starting this frame...
            if ccimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ccimage.frameNStart = frameN  # exact frame index
                ccimage.tStart = t  # local t and not account for scr refresh
                ccimage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ccimage, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ccimage.started')
                # update status
                ccimage.status = STARTED
                ccimage.setAutoDraw(True)
            
            # if ccimage is active this frame...
            if ccimage.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                screen_scale_keys.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in screen_scale_keys.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "screen_scale_keys" ---
        for thisComponent in screen_scale_keys.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for screen_scale_keys
        screen_scale_keys.tStop = globalClock.getTime(format='float')
        screen_scale_keys.tStopRefresh = tThisFlipGlobal
        # Run 'End Routine' code from scale_keys_code
        thisExp.addData('X Scale',x_scale)
        thisExp.addData('Y Scale',y_scale)
        # the Routine "screen_scale_keys" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "rectangle_keys" ---
        # create an object to store info about Routine rectangle_keys
        rectangle_keys = data.Routine(
            name='rectangle_keys',
            components=[rectangle_text, polygon_keys, key_resp_keys],
        )
        rectangle_keys.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        polygon_keys.setSize((10*x_scale, 10*y_scale))
        # create starting attributes for key_resp_keys
        key_resp_keys.keys = []
        key_resp_keys.rt = []
        _key_resp_keys_allKeys = []
        # store start times for rectangle_keys
        rectangle_keys.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        rectangle_keys.tStart = globalClock.getTime(format='float')
        rectangle_keys.status = STARTED
        rectangle_keys.maxDuration = None
        # keep track of which components have finished
        rectangle_keysComponents = rectangle_keys.components
        for thisComponent in rectangle_keys.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "rectangle_keys" ---
        # if trial has changed, end Routine now
        if isinstance(key_scale, data.TrialHandler2) and thisKey_scale.thisN != key_scale.thisTrial.thisN:
            continueRoutine = False
        rectangle_keys.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rectangle_text* updates
            
            # if rectangle_text is starting this frame...
            if rectangle_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rectangle_text.frameNStart = frameN  # exact frame index
                rectangle_text.tStart = t  # local t and not account for scr refresh
                rectangle_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rectangle_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                rectangle_text.status = STARTED
                rectangle_text.setAutoDraw(True)
            
            # if rectangle_text is active this frame...
            if rectangle_text.status == STARTED:
                # update params
                pass
            
            # *polygon_keys* updates
            
            # if polygon_keys is starting this frame...
            if polygon_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_keys.frameNStart = frameN  # exact frame index
                polygon_keys.tStart = t  # local t and not account for scr refresh
                polygon_keys.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_keys, 'tStartRefresh')  # time at next scr refresh
                # update status
                polygon_keys.status = STARTED
                polygon_keys.setAutoDraw(True)
            
            # if polygon_keys is active this frame...
            if polygon_keys.status == STARTED:
                # update params
                pass
            
            # *key_resp_keys* updates
            waitOnFlip = False
            
            # if key_resp_keys is starting this frame...
            if key_resp_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_keys.frameNStart = frameN  # exact frame index
                key_resp_keys.tStart = t  # local t and not account for scr refresh
                key_resp_keys.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_keys, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_keys.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_keys.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_keys.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_keys.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_keys_allKeys.extend(theseKeys)
                if len(_key_resp_keys_allKeys):
                    key_resp_keys.keys = _key_resp_keys_allKeys[-1].name  # just the last key pressed
                    key_resp_keys.rt = _key_resp_keys_allKeys[-1].rt
                    key_resp_keys.duration = _key_resp_keys_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                rectangle_keys.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rectangle_keys.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "rectangle_keys" ---
        for thisComponent in rectangle_keys.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for rectangle_keys
        rectangle_keys.tStop = globalClock.getTime(format='float')
        rectangle_keys.tStopRefresh = tThisFlipGlobal
        # check responses
        if key_resp_keys.keys in ['', [], None]:  # No response was made
            key_resp_keys.keys = None
        key_scale.addData('key_resp_keys.keys',key_resp_keys.keys)
        if key_resp_keys.keys != None:  # we had a response
            key_scale.addData('key_resp_keys.rt', key_resp_keys.rt)
            key_scale.addData('key_resp_keys.duration', key_resp_keys.duration)
        # the Routine "rectangle_keys" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1.0 repeats of 'key_scale'
    
    
    # --- Prepare to start Routine "Instruction" ---
    # create an object to store info about Routine Instruction
    Instruction = data.Routine(
        name='Instruction',
        components=[text_inst, instr_key],
    )
    Instruction.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for instr_key
    instr_key.keys = []
    instr_key.rt = []
    _instr_key_allKeys = []
    # store start times for Instruction
    Instruction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instruction.tStart = globalClock.getTime(format='float')
    Instruction.status = STARTED
    Instruction.maxDuration = None
    # keep track of which components have finished
    InstructionComponents = Instruction.components
    for thisComponent in Instruction.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instruction" ---
    Instruction.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_inst* updates
        
        # if text_inst is starting this frame...
        if text_inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_inst.frameNStart = frameN  # exact frame index
            text_inst.tStart = t  # local t and not account for scr refresh
            text_inst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_inst, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_inst.status = STARTED
            text_inst.setAutoDraw(True)
        
        # if text_inst is active this frame...
        if text_inst.status == STARTED:
            # update params
            pass
        
        # *instr_key* updates
        waitOnFlip = False
        
        # if instr_key is starting this frame...
        if instr_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_key.frameNStart = frameN  # exact frame index
            instr_key.tStart = t  # local t and not account for scr refresh
            instr_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_key, 'tStartRefresh')  # time at next scr refresh
            # update status
            instr_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instr_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instr_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instr_key.status == STARTED and not waitOnFlip:
            theseKeys = instr_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _instr_key_allKeys.extend(theseKeys)
            if len(_instr_key_allKeys):
                instr_key.keys = _instr_key_allKeys[-1].name  # just the last key pressed
                instr_key.rt = _instr_key_allKeys[-1].rt
                instr_key.duration = _instr_key_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instruction.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instruction.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instruction" ---
    for thisComponent in Instruction.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instruction
    Instruction.tStop = globalClock.getTime(format='float')
    Instruction.tStopRefresh = tThisFlipGlobal
    thisExp.nextEntry()
    # the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler2(
        name='trials',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions(subCond), 
        seed=None, 
    )
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "block" ---
        # create an object to store info about Routine block
        block = data.Routine(
            name='block',
            components=[text, key_resp],
        )
        block.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_resp
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # Run 'Begin Routine' code from code_2
        # by default skip the routine:
        continueRoutine = False
        
        # on trial 0 → practice message
        if trials.thisTrialN == 0:
            Block_text = 'Practice will start. Please press space bar to continue.'
            continueRoutine = True
        
        # at the end of practice
        elif trials.thisTrialN == practice_count:
            Block_text = 'Formal Experiment will start. Please press space bar to continue.'
            continueRoutine = True
        # after the first FormalTrials
        elif trials.thisTrialN == practice_count + n_trl:
            Block_text = 'You did a great job, please take a rest. Press space bar to continue to next block.'
            continueRoutine = True
        
        # store start times for block
        block.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        block.tStart = globalClock.getTime(format='float')
        block.status = STARTED
        block.maxDuration = None
        # keep track of which components have finished
        blockComponents = block.components
        for thisComponent in block.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "block" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        block.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                text.setText(Block_text, log=False)
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                block.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in block.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "block" ---
        for thisComponent in block.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for block
        block.tStop = globalClock.getTime(format='float')
        block.tStopRefresh = tThisFlipGlobal
        # the Routine "block" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Encoding" ---
        # create an object to store info about Routine Encoding
        Encoding = data.Routine(
            name='Encoding',
            components=[stimulus_grating, fixation],
        )
        Encoding.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_encoding
        orientation = randint(1,180)
        
        # store start times for Encoding
        Encoding.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Encoding.tStart = globalClock.getTime(format='float')
        Encoding.status = STARTED
        Encoding.maxDuration = None
        # keep track of which components have finished
        EncodingComponents = Encoding.components
        for thisComponent in Encoding.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Encoding" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        Encoding.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stimulus_grating* updates
            
            # if stimulus_grating is starting this frame...
            if stimulus_grating.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                stimulus_grating.frameNStart = frameN  # exact frame index
                stimulus_grating.tStart = t  # local t and not account for scr refresh
                stimulus_grating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimulus_grating, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimulus_grating.started')
                # update status
                stimulus_grating.status = STARTED
                stimulus_grating.setAutoDraw(True)
            
            # if stimulus_grating is active this frame...
            if stimulus_grating.status == STARTED:
                # update params
                stimulus_grating.setOri(orientation, log=False)
            
            # if stimulus_grating is stopping this frame...
            if stimulus_grating.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stimulus_grating.tStartRefresh + duration-frameTolerance:
                    # keep track of stop time/frame for later
                    stimulus_grating.tStop = t  # not accounting for scr refresh
                    stimulus_grating.tStopRefresh = tThisFlipGlobal  # on global time
                    stimulus_grating.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stimulus_grating.stopped')
                    # update status
                    stimulus_grating.status = FINISHED
                    stimulus_grating.setAutoDraw(False)
            
            # *fixation* updates
            
            # if fixation is starting this frame...
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                # update status
                fixation.status = STARTED
                fixation.setAutoDraw(True)
            
            # if fixation is active this frame...
            if fixation.status == STARTED:
                # update params
                pass
            
            # if fixation is stopping this frame...
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation.frameNStop = frameN  # exact frame index
                    # update status
                    fixation.status = FINISHED
                    fixation.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Encoding.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Encoding.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Encoding" ---
        for thisComponent in Encoding.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Encoding
        Encoding.tStop = globalClock.getTime(format='float')
        Encoding.tStopRefresh = tThisFlipGlobal
        # the Routine "Encoding" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "cue_to_reproduce" ---
        # create an object to store info about Routine cue_to_reproduce
        cue_to_reproduce = data.Routine(
            name='cue_to_reproduce',
            components=[rep_cue],
        )
        cue_to_reproduce.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for cue_to_reproduce
        cue_to_reproduce.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        cue_to_reproduce.tStart = globalClock.getTime(format='float')
        cue_to_reproduce.status = STARTED
        cue_to_reproduce.maxDuration = None
        # keep track of which components have finished
        cue_to_reproduceComponents = cue_to_reproduce.components
        for thisComponent in cue_to_reproduce.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "cue_to_reproduce" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        cue_to_reproduce.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.6:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rep_cue* updates
            
            # if rep_cue is starting this frame...
            if rep_cue.status == NOT_STARTED and tThisFlip >= .3-frameTolerance:
                # keep track of start time/frame for later
                rep_cue.frameNStart = frameN  # exact frame index
                rep_cue.tStart = t  # local t and not account for scr refresh
                rep_cue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rep_cue, 'tStartRefresh')  # time at next scr refresh
                # update status
                rep_cue.status = STARTED
                rep_cue.setAutoDraw(True)
            
            # if rep_cue is active this frame...
            if rep_cue.status == STARTED:
                # update params
                pass
            
            # if rep_cue is stopping this frame...
            if rep_cue.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rep_cue.tStartRefresh + .3-frameTolerance:
                    # keep track of stop time/frame for later
                    rep_cue.tStop = t  # not accounting for scr refresh
                    rep_cue.tStopRefresh = tThisFlipGlobal  # on global time
                    rep_cue.frameNStop = frameN  # exact frame index
                    # update status
                    rep_cue.status = FINISHED
                    rep_cue.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                cue_to_reproduce.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cue_to_reproduce.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "cue_to_reproduce" ---
        for thisComponent in cue_to_reproduce.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for cue_to_reproduce
        cue_to_reproduce.tStop = globalClock.getTime(format='float')
        cue_to_reproduce.tStopRefresh = tThisFlipGlobal
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if cue_to_reproduce.maxDurationReached:
            routineTimer.addTime(-cue_to_reproduce.maxDuration)
        elif cue_to_reproduce.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.600000)
        
        # --- Prepare to start Routine "Reproduction" ---
        # create an object to store info about Routine Reproduction
        Reproduction = data.Routine(
            name='Reproduction',
            components=[gabor],
        )
        Reproduction.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_reproduction
        # clear any stray events, and reset our flags/timers
        kb.clearEvents()
        #event.clearEvents(eventType='keyboard')
        
        keyPressed   = False
        keyReleased = False
        keyOnset     = None
        repDuration  = None
        
        # store start times for Reproduction
        Reproduction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Reproduction.tStart = globalClock.getTime(format='float')
        Reproduction.status = STARTED
        Reproduction.maxDuration = None
        # keep track of which components have finished
        ReproductionComponents = Reproduction.components
        for thisComponent in Reproduction.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Reproduction" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        Reproduction.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *gabor* updates
            
            # if gabor is starting this frame...
            if gabor.status == NOT_STARTED and keyPressed:
                # keep track of start time/frame for later
                gabor.frameNStart = frameN  # exact frame index
                gabor.tStart = t  # local t and not account for scr refresh
                gabor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(gabor, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'gabor.started')
                # update status
                gabor.status = STARTED
                gabor.setAutoDraw(True)
            
            # if gabor is active this frame...
            if gabor.status == STARTED:
                # update params
                gabor.setOri(orientation, log=False)
            
            # if gabor is stopping this frame...
            if gabor.status == STARTED:
                if bool(keyReleased):
                    # keep track of stop time/frame for later
                    gabor.tStop = t  # not accounting for scr refresh
                    gabor.tStopRefresh = tThisFlipGlobal  # on global time
                    gabor.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'gabor.stopped')
                    # update status
                    gabor.status = FINISHED
                    gabor.setAutoDraw(False)
            # Run 'Each Frame' code from code_reproduction
            # poll for space‐bar down & up, waiting for the release event
            keys = kb.getKeys(keyList=['down'], waitRelease=False, clear = False)
            
            for k in keys:
                # ─ key down ─
                if (k.duration is None) and not keyPressed:
                    keyPressed = True
                    if keyOnset is None:
                        keyOnset   =  globalClock.getTime()
            
            if keyPressed:
                if not keys:
                    keyReleased = True
                    keyOffset = globalClock.getTime()
                    repDuration = keyOffset - keyOnset
                    continueRoutine = False        # finish this trial
            
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Reproduction.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Reproduction.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Reproduction" ---
        for thisComponent in Reproduction.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Reproduction
        Reproduction.tStop = globalClock.getTime(format='float')
        Reproduction.tStopRefresh = tThisFlipGlobal
        # Run 'End Routine' code from code_reproduction
        # log the key‐hold data
        thisExp.addData('orientation', orientation)  
        thisExp.addData('rpr_onset',   keyOnset)  
        thisExp.addData('rpr_duration', repDuration)
        # the Routine "Reproduction" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        # create an object to store info about Routine feedback
        feedback = data.Routine(
            name='feedback',
            components=[feedback_text],
        )
        feedback.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from feedback_code
        error_ratio = np.abs(repDuration/duration -1)
        
        if error_ratio > 0.3:
            fb_text = "Your key pressed duration deviated too far!"
        else:
            fb_text = ''
        # store start times for feedback
        feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        feedback.tStart = globalClock.getTime(format='float')
        feedback.status = STARTED
        thisExp.addData('feedback.started', feedback.tStart)
        feedback.maxDuration = None
        # skip Routine feedback if its 'Skip if' condition is True
        feedback.skipped = continueRoutine and not (trials.thisTrialN >= practice_count)
        continueRoutine = feedback.skipped
        # keep track of which components have finished
        feedbackComponents = feedback.components
        for thisComponent in feedback.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        feedback.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.8:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text* updates
            
            # if feedback_text is starting this frame...
            if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text.frameNStart = frameN  # exact frame index
                feedback_text.tStart = t  # local t and not account for scr refresh
                feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text.started')
                # update status
                feedback_text.status = STARTED
                feedback_text.setAutoDraw(True)
            
            # if feedback_text is active this frame...
            if feedback_text.status == STARTED:
                # update params
                feedback_text.setText(fb_text, log=False)
            
            # if feedback_text is stopping this frame...
            if feedback_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_text.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_text.tStop = t  # not accounting for scr refresh
                    feedback_text.tStopRefresh = tThisFlipGlobal  # on global time
                    feedback_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text.stopped')
                    # update status
                    feedback_text.status = FINISHED
                    feedback_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                feedback.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedback.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for feedback
        feedback.tStop = globalClock.getTime(format='float')
        feedback.tStopRefresh = tThisFlipGlobal
        thisExp.addData('feedback.stopped', feedback.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if feedback.maxDurationReached:
            routineTimer.addTime(-feedback.maxDuration)
        elif feedback.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.800000)
        
        # --- Prepare to start Routine "iti" ---
        # create an object to store info about Routine iti
        iti = data.Routine(
            name='iti',
            components=[iti_blank],
        )
        iti.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for iti
        iti.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        iti.tStart = globalClock.getTime(format='float')
        iti.status = STARTED
        iti.maxDuration = None
        # keep track of which components have finished
        itiComponents = iti.components
        for thisComponent in iti.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "iti" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        iti.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *iti_blank* updates
            
            # if iti_blank is starting this frame...
            if iti_blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                iti_blank.frameNStart = frameN  # exact frame index
                iti_blank.tStart = t  # local t and not account for scr refresh
                iti_blank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(iti_blank, 'tStartRefresh')  # time at next scr refresh
                # update status
                iti_blank.status = STARTED
                iti_blank.setAutoDraw(True)
            
            # if iti_blank is active this frame...
            if iti_blank.status == STARTED:
                # update params
                pass
            
            # if iti_blank is stopping this frame...
            if iti_blank.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > iti_blank.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    iti_blank.tStop = t  # not accounting for scr refresh
                    iti_blank.tStopRefresh = tThisFlipGlobal  # on global time
                    iti_blank.frameNStop = frameN  # exact frame index
                    # update status
                    iti_blank.status = FINISHED
                    iti_blank.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                iti.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in iti.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "iti" ---
        for thisComponent in iti.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for iti
        iti.tStop = globalClock.getTime(format='float')
        iti.tStopRefresh = tThisFlipGlobal
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if iti.maxDurationReached:
            routineTimer.addTime(-iti.maxDuration)
        elif iti.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "Goodbye" ---
    # create an object to store info about Routine Goodbye
    Goodbye = data.Routine(
        name='Goodbye',
        components=[goodbye_text, goodbye_key],
    )
    Goodbye.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for goodbye_key
    goodbye_key.keys = []
    goodbye_key.rt = []
    _goodbye_key_allKeys = []
    # store start times for Goodbye
    Goodbye.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Goodbye.tStart = globalClock.getTime(format='float')
    Goodbye.status = STARTED
    Goodbye.maxDuration = None
    # keep track of which components have finished
    GoodbyeComponents = Goodbye.components
    for thisComponent in Goodbye.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Goodbye" ---
    Goodbye.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *goodbye_text* updates
        
        # if goodbye_text is starting this frame...
        if goodbye_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            goodbye_text.frameNStart = frameN  # exact frame index
            goodbye_text.tStart = t  # local t and not account for scr refresh
            goodbye_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(goodbye_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            goodbye_text.status = STARTED
            goodbye_text.setAutoDraw(True)
        
        # if goodbye_text is active this frame...
        if goodbye_text.status == STARTED:
            # update params
            pass
        
        # *goodbye_key* updates
        waitOnFlip = False
        
        # if goodbye_key is starting this frame...
        if goodbye_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            goodbye_key.frameNStart = frameN  # exact frame index
            goodbye_key.tStart = t  # local t and not account for scr refresh
            goodbye_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(goodbye_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'goodbye_key.started')
            # update status
            goodbye_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(goodbye_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(goodbye_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if goodbye_key.status == STARTED and not waitOnFlip:
            theseKeys = goodbye_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _goodbye_key_allKeys.extend(theseKeys)
            if len(_goodbye_key_allKeys):
                goodbye_key.keys = _goodbye_key_allKeys[-1].name  # just the last key pressed
                goodbye_key.rt = _goodbye_key_allKeys[-1].rt
                goodbye_key.duration = _goodbye_key_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Goodbye.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Goodbye.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Goodbye" ---
    for thisComponent in Goodbye.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Goodbye
    Goodbye.tStop = globalClock.getTime(format='float')
    Goodbye.tStopRefresh = tThisFlipGlobal
    # check responses
    if goodbye_key.keys in ['', [], None]:  # No response was made
        goodbye_key.keys = None
    thisExp.addData('goodbye_key.keys',goodbye_key.keys)
    if goodbye_key.keys != None:  # we had a response
        thisExp.addData('goodbye_key.rt', goodbye_key.rt)
        thisExp.addData('goodbye_key.duration', goodbye_key.duration)
    thisExp.nextEntry()
    # the Routine "Goodbye" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
