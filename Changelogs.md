>## 1.5.2 - INITIAL PUBLIC RELEASE

>## 1.5.3 - HOTFIX
    * Improved Decal machine material support
    * Automatic decal subdivision
    * Removed edge control(redudant due to decal margin)
    * New bakesets are now added to bottom instead of top

>## 1.6.0 - QOL UPDATE
    * UDIMS are now automatically detected from UV map
    * UDIMS resolution rules added to bake set settings
    * New bake units are now added to the bottom instead of top
    * bake sets can now have multiple bake types!
    * bake sets that don't use the alpha channel will default to 1.0 alpha correctly.
    * Channel selector is now aligned
    * Bake denoise/blur strength moved to bakeset settings.
    * Hide option added to bake unit
    * Cancel option added to baking (E+Ctrl)
    * Fixed Shapekey ignore not working when using decals.
    * High to Low baking no longer requires overlapping.

>## 1.6.1 - HOTFIX
    * Fixed broken imports
    * Fixed some scene parameters being modified after bake

>## 1.6.2 - BUGFIXES
    * Bakeunit hide toggle is no longer inverted.
    * Bake isolated mode no longer hides objects after the bake.

>## 1.6.3 - STABILITY UPDATE 2/3/2024
    * Use sanity check moved to addon properties
    * Ability to bake Glossy
    * Forcing bake ray cast mode to Above Surface to ensure consistency
    * Hidden objects no longer cause bake to fail

>## 1.6.4 - STABILITY UPDATE 31/3/2024
    * Hidden objects causing errors fixed
    * Materials without nodes are now handeled
    * Blender 4.1 support

>## 1.6.5 - STABILITY UPDATE 26/4/2024
    * Fixed problem where channel packing results in missing alpha in certain situations
    * Fixed an edge case where objects with vertices only on uv borders fail to bake

>## 1.7.25 - NEW FEATURES 8/6/2024
    * Low object selection can be toggled to be a Low object collection instead
    * Decal baking now has an toggle for including the underlying object automatically.
    * Finalize baked objects for export
    * Automatic Suffix generation
    * MacOS/Linux Support
    * Many small bugfixes

>## 1.7.26 - QOL UPDATE 13/6/2024
    * UcuPainter support
    * Ability to quickly bake in texture painting mode

>## 1.7.28 - Stability UPDATE 20/6/2024
    * Embedded import packages. Ensures version stability

>## 1.7.30 - NEW  FEATURES UPDATE 21/6/2024
    * More robust material parser algorithm
    * Support for Stamp It! https://blendermarket.com/products/easy-decal--stamp

>## 1.7.67 - NEW FEATURES 25/6/2024
    * Sanctus Library decal materials baking fixed
    * Search feature(affects Finalize and Bake all Sets)
    * Even more robust material parser algorithm

>## 1.7.68 - Stability 26/6/2024
    * Fixed decalMACHINE regression


>## 1.7.70 - NEW FEATURES 28/6/2024
    * Added a sharpen post-process effect
    * Bugfixes to post-process effects

>## 1.7.74 - Bugfixes 28/6/2024
    * Alpha blending now works correctly
    * Bugfixes to post-process effects


>## 1.7.80 - Hotfix 1/7/2024
    * BSDF fetcher related crashes fixed
    * Baked normals being affected by diffuse

>## 1.7.82 - NEW FEATURES 20/7/2024
    * Post Process effects now utilize Blenders internal compositor
    * New Post Process filters. Kuwahara filter + Antialias

>## 1.7.84 - CHANGE 23/7/2024
    * Folder open parameter changed to open baked images in blender instead.
    * small bugfixes


>## 1.7.85 - HOTFIX 23/7/2024
    * Fixed opening new windows with bakes

>## 1.7.90 - NEW FATURES 1/8/2024
    * Smoothness type added
    * Position type added
    * Ability to specify suffixes 

>## 1.7.91 - HOTFIX 3/8/2024
    * Alphas no longer get premultiplied with RGB channels when baking using channel packing

>## 1.7.92 - HOTFIX 13/8/2024
    * Non-Fixed aspect ratio now works correctly
    * Alpha channel packing fixed for custom types

>## 1.8.0 - Profile Update 11/10/2024
    * Improved Addon stability and UI performance
    * Bake Set Settings are now replaced with profiles
    * Bake Types are now stored in profiles
    * Profile Saving/Loading
    * Ambient occlusion baking is now split into two bake types.(Ambient Occlusion and Thickness)[This allows you to bake both types in a single profile]
    * Normal Baking is now split into two bake types.(Normal and World Space Normal)[This allows you to bake both types in a single profile]
    * Deprecating Linked Bakesets(bake sets that are identical will bake together)[Makes addon more stable]
    * Deprecating Drivers(Pointless now that we can use profiles)[Makes addon more stable]


>## 1.8.1 - Hotfix 14/10/2024
    * Kuwahara setting names fixed
    * Image aspect ratio toggle moved inside profile
    * Changed default extrusion from 0.1m to 0.02m
    * Changed post process effect icons back to original ones
    * Fixed Post process effect text to match old
    * added OSL checks
    * Combined Ultibake + BakeSets panel into one
    * Icons for each panel
    * Documentation now in panel header

>## 1.8.2 - Improvements and Bugfixes 15/10/2024
    * Removed isolation mode. Replaced with Blender's native Render toggles
    * Hiding isn't controlled by the addon anymore.
    * Fixed special bakes not baking to alpha channel
    * Fixed crash caused by context problems
    * Decal projection now using normal based projection mode
    * Documentation button is now smaller
    * Fixed Searching
    * Finalize check added for multiple unique texture names
    * OSL check removed(way too laggy)


>## 1.8.3 - Bugfixes 20/10/2024
    * OSL check removed(way too laggy)
    * Decals suffixed with "_PROJ" or ".PROJ" will now use a different projection mode
        * This can improve decal quality in most cases, except for Fonts where it will do the opposite.
    * Decal subdivision threshold lowered from 1024 to 10, this caused many of the lag issues when using decal baking.
    * Don't open baked images when force exit
    * Setting an invalid mesh object in low,high,cage and decals wont brick the addon anymore.
    * Font baking works without converting it to object



>## 1.8.4 - Optimizations 24/10/2024
    * Debugging is now disabled by default(bpy.context.scene.sna_skipdebug = True to enable)
    * Added parameter to disable Automatic UDIM detection


>## 1.8.5 - Bugfix 2/11/2024
    * Custom texture suffixes didn't get detected.
    * AO visibility by collection is fixed


>## 1.8.6 - Bugfix 25/11/2024
    * Icons fixed
    * Texture set alphas affect other texture sets fixed


>## 1.8.7-8 - Improvement 25/11/2024
    * Icons fixes
    * Quality slider added to profiles


>## 1.8.9 - Bugfix 06/12/2024
    * Decal blending fixed with black masks
    * Finalize now applies textures correctly


>## 1.8.10 - Addition 06/12/2024
    * Added object fix button(described in documentation)

>## 1.8.11 - Bugfix 28/12/2024
    * Color settings do not affect the bakes now

>## 1.8.12 - Rework 11/01/2025
    * Panel rework
    * Moving away from SNA

>## 1.8.13 - Rework 11/01/2025
    * UI rework
    * Alpha blending fixed for stamps, no longer goes to black

>## 1.8.14 - Rework 16/01/2025
    * Reworked how decals are applied internally to support floating meshes
    * removed stack height parameter(obsolete)
    * removed alpha sensitivity parameter(obsolete due to stamp stencils)
    * UI re-shuffle
    * UI panel is now called Ultikynnys instead of Ultibake to keep panel amount low when using multiple Ultikynnys addons


>## 1.8.15 - Hotfix 17/01/2025
    * Addon loading/saving no longer errors out


>## 1.8.16 - Hotfix 18/01/2025
    * Alpha smoothing no longer errors out
    * Emission baking fixed from regression 




>## 1.8.17 - Hotfix 20/01/2025
    * Normal map smoothing now works correctly when using float mesh decals, Normal directionality fixed when using mesh decals

>## 1.8.18 - Hotfix 20/01/2025
    * Normal map direction fixed for image projection



>## 1.8.19 - Hotfix 20/01/2025
    * all except for anisotrophic kuwahara filtering replaced with scipy post processing effects


    
>## 1.8.20 - Woooooo Hotfix 20/01/2025
    * Changed Gpu baking icon to ENUM
    * Fixed regression bug with using cage object when baking
    * Fixed empty texture units causing problems
    

>## 1.8.23 - General bugfixes 27/01/2025
    * Fixed issue with installing dependencies

>## 1.8.27 - General bugfixes 05/02/2025
    * Added local mode to AO and Thickness
    * various small bugfixes



>## 1.8.27 - General bugfixes 05/02/2025
    * More safety checks for advanced setups


>## 1.8.33 - General bugfixes 05/02/2025
    * UI rework
    * More guards
    * Post processing fixed
    * Slightly faster bake times
  

>## 1.9.0 - Version Increment 15/02/2025
    * Pre-bake Visualizer Added
    * UDIM visualizer added
    * Bake Set Generator Added
    * UI rework
    * Many many small fixes
    * Normalized Position baking now can be split to R G B channels
    * Bake progress now visible inside Blender
    * Added Ability to stop the bake on non-Windows Machines with ESC

>## 1.9.2 - Hotfix 16/02/2025
    * diffuse baking with broken normal fixed


>## 1.9.4 - Hotfix 16/02/2025
    * antialias no longer makes alpha channel bakes darker


>## 1.9.11 - Hotfix 17/02/2025
    * Normal map baking works fine now
    * Decals to Low baking works without high object now


>## 1.9.12 - Hotfix 18/02/2025
    * Decal baking doesn't suffer from cage distortions


>## 1.9.14 - Hotfix 18/02/2025
    * mesh data reset for invalid decals result better decal stability


>## 1.9.15 - Hotfix 22/02/2025
    * Temporary image nodes are now removed from materials

>## 1.9.16 - Hotfix 23/02/2025
    * Progress bar now doesn't start with previous bake information

>## 1.9.17 - Hotfix 28/02/2025
    * Decals no longer cast AO or Shadows

>## 1.9.20 - Addition 18/03/2025
    * Bent Normal Bake type added

>## 1.9.21 - Hotfix 19/03/2025
    * Bent Normal tangent space bakes correctly now


>## 1.9.23 - Addition 31/03/2025
    * Button added to clear baked texture folder
    * Bake folder filesize now displayed

>## 1.9.24 - Addition 3/04/2025
    * API call added bpy.ops.api.run_ultibake()


>## 1.9.25 - General Fixes 24/05/2025
    * Various small bug fixes
    * Console Progress bar now deprecated due to UI upgrade
    * Console toggle removed
    * Blender 3 regression fix
    * A channel packing fixed

>## 1.9.27 - Hotfix 24/05/2025
    * Saved textures which do not update after first bake
    * Added 16-bit png baking (use .exr if using alpha channel packing)


>## 1.9.27 - Addition 26/05/2025
    * Automatic Updates added



>## 1.9.34 - Addition 29/05/2025
    * Fixing various regressions
    * 16-bit button deprecated, all bakes are 16 bit as long as the format supports it.
    * 20% faster bakes

>## 1.9.38 - Hotfix 29/05/2025
    * Fixed depedency crash
    * Mesh finalize now shows non-color textures correctly
    * Fix UI

>## 1.9.39 - Stability Update 31/05/2025
    * Removed redundant systems and parameters
    * Better stability
    * Fixed various colorspace issues

>## 1.9.44 - Stability Update 31/05/2025
    * Hardening post bake scene to prevent crashing


>## 1.9.45 - Stability Update 31/05/2025
    * Fixed Keep Only Active UVmaps error
    * update changelogs now visible from UI


>## 1.9.46 - Stability Update 31/05/2025
    * Ensuring stability for updates and changelog visualization


>## 1.9.47 - Hotfix 31/05/2025
    * Fixed Finalize not working with relative folder paths

>## 1.9.48 - Hotfix 31/05/2025
    * Enforcing non-color for image nodes in finalize


>## 1.9.51 - Addition 31/05/2025
    * Print messages no longer get hijacked to have the [Ultibake] prefix
    * New override for controlling the use_cage parameter which affects normal skew


>## 1.9.52 - Improvement 1/06/2025
    * use_cage override parameter now a 3-state enum


>## 1.9.55 - Hotfix 2/06/2025
    * 8% faster bakes
    * Finalize now works with UDIMs

>## 1.9.56 - Addition 2/06/2025
    * More tooltips added


>## 1.9.57 - Hotfix 2/06/2025
    * Fixed UDIM visualizer

>## 1.9.58 - Improvement 2/06/2025
    * Unified Sample Control implemented


>## 1.9.60 - Improvement 3/06/2025
    * Anisotropic Kuwahara filtering reworked
