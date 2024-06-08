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

>## 1.7.24 - NEW FEATURES 8/6/2024
    * Low object selection can be toggled to be a Low object collection instead
    * Decal baking now has an toggle for including the underlying object automatically.
    * Finalize baked objects for export
    * Automatic Suffix generation
    * MacOS/Linux Support
    * Many small bugfixes
