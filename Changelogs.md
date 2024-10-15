# Changelogs

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
    