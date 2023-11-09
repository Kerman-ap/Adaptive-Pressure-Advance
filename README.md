# Adaptive-Pressure-Advance
Speed dependent pressure advance for Klipper

Maybe have a look at the advanced-features fork first, which corrects for this issue 

https://github.com/dmbutyugin/klipper/tree/advanced-features

Otherwise, you can do it in gcode with this method


Corrects for [this](https://www.reddit.com/r/klippers/comments/o98xes/pressure_advance_becomes_way_too_aggressive_when/) issue:
- Klipper will make pressure too aggressive at high speeds, and not aggressive enough at lower speeds
- This has a large impact on speed-quality printing, when you are trying to be conservative on outer surfaces and rushing infil, etc

# Usage #
Add as a post-processing script in superslicer/prusaslicer

Change settings in the script (tuningspeed should be the speed yoou calibrated pressure advance for)

# Issues #
- Changing pressure advance on the fly seens to do some funky stuff






