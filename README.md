## Showcase
> The following video will showcase most of the important features of Ultibake and quickly how to use the addon. [Click here for more information](#Usage)

<iframe width="300em" height="200em" src="https://www.youtube.com/embed/A-00q0g_X5k"allowfullscreen></iframe>

## Latest Update
<iframe width="300em" height="200em" src="https://www.youtube.com/embed/bVQO3cXhhyc"allowfullscreen></iframe>

### High to Low baking

> Baking high detail objects to low poly representations is a very common trick to getting assets to run in real-time applications. The following video will cover this topic.

<iframe width="300em" height="200em" src="https://www.youtube.com/embed/gd659C732qs"allowfullscreen></iframe>


### Decal Baking

> Allows you to project any image to a low poly object. Even works if the image uses multiple masks like Normals,roughness,metallic etc. 

> DecalMachine materials use a parallax node, which needs to be disabled from the material

<iframe width="300em" height="200em" src="https://www.youtube.com/embed/3LwLf0DBy1A"allowfullscreen></iframe>

> For TrimFlow users, this is how you setup the bake. All you need to do is move the generated decal mesh into a decal collection which is used by the Bake Set

![alt text](image-20.webp)

### Decal Stacking

> Allows you to stack decals on top of each other with control over stack order.

> The Alphastack.blend file comes with the addon.

<iframe width="300em" height="200em" src="https://www.youtube.com/embed/ltRfZqC-O6g"allowfullscreen></iframe>


### Udims

> While Ultibake handels UDIM baking automatically, this video explains how it can be used. This video also explains several extra considerations when working with decals, like how to fix decal seams and black borders.

<iframe width="300em" height="200em" src="https://www.youtube.com/embed/Mzp5L5xpPIg"allowfullscreen></iframe>

# Usage

The addon introduces various terms, which are explained here.

## Bake Sets

> **Bake Sets** are the most important part of the addon. These containers can be created/removed and they contain all the information that specify what objects will be baked into textures. They can be individually baked for time save or you can bake all of them from the **Bake All Sets** Button

> The **Search feature** will affect how **Bake All Sets** works, so you can use it to filter specific **Bake Sets** 

![alt text](Search.webp)

> You can have as many **Bake Sets** as you want.

> **Bake Sets are tied to a Scene**, so you can have multiple setups if you utilize multiple Scenes. **Great for reducing clutter**

## Profiles

> Added in 1.8 This is the new way of defining **what** textures will be baked and **how** for **Bake Sets** It works the same was in 1.7, but the settings and type information has been moved here.

![alt text](image-6.png)

> You can also save profiles to an external file. This way you can re-use these profiles in any Blender project.

![alt text](parsecd_jPDlh803v3.png)

## Profile parameters

![alt text](image-7.png)


* **Margin** - extra padding from the UV island borders, which prevent seams when dealing with LODs

* **XY** - The dimensions of the image that will be baked, can be toggled with the **Fixed Aspect Ratio** button to expose X and Y separately

* **Cage Extrusion** - How much to inflate the **Cage** object, useful for tweaking **High** to **Low** baking

* **Max Ray Distance** - How far can a ray be cast from a **High** object when projected to a **Low** object.

* **Bake Samples Per Pixel** - Controls how many passes each pixel in the baked texture will get during the baking. It's a good idea to **set this to a low value**, due to its **impact on bake time**

## Post-Process Effects

> These are applied after the bake. The effects stack and they are applied in top to bottom order.

![alt text](image-8.png)

![alt text](blender_k9uN6Kpcmw.webp)
![alt text](blender_Bdz51vaJ2N.webp)
![alt text](blender_Uqpi6DzJeo.webp)
![alt text](blender_yflZLdZMJD.webp)
![alt text](blender_USdIiTlX8M.webp)

## UDIMS

* **Add Udim Scale Rule Button** - Adds a resolution multiplier to any UV Islands that are in the corresponding UDIM tile

![alt text](blender_30zS0uqnk4.gif)

> **UDIMS are handeled automatically by Ultibake**, so you only have to ensure that the UV Islands are packed in the correct tiles. I highly recommend UVPackmaster3 for this.

![alt text](image-11.png)

## Bake Units

>    With **Bake Units** we can define the **objects which are used for baking**. It also contains the target UVmap which is required for the bake. a **Bake Set** can contain any amount of **Bake Units**, which allows you to easily bake multiple objects for each profile.

![alt text](image-14.png)

![alt text](image-12.png)

* **Low** - the object/collection which will be baked
> Uses the UVmap selector shown in the image below

* **High** - the object which will be projected to the surface of the **Low** object
> Commonly used for baking high detail meshes to low poly representations

* **Cage** - the object which will define how the projection from **High** to **Low** baking will behave
> optional, rarely needed, but useful for complicated high to low bakes

* **Decals** - the collection which will have its meshes projected to the **Low** object
> Similar to High to Low baking, but contains internal pre-processing to ensure better results

> Any non-mesh based decal method like with the "Stamp It!" Addon does not require the decal collection, since its applied directly to the material.

* **Decals Only Toggle** - This will as it name implies, bake the **Decals** to the **Low** object, but not the underlying **Low** Object itself.
> Useful when your application requires you to apply decals on top of an existing texture

* **Collection Toggle** - a toggle which will convert the **Low** parameter to a collection instead
> This will prevent you from using High to Low baking or Decals, but its crucial for bakes that contain many objects

* **Baking UV map** - Convenient selector for choosing what UVmap to use for the **Low** object or **Low** collection.
> With collections it will only show UVmaps that are shared with all the other objects in the low collection

![alt text](blender_uyiswEQhRE.gif)

## Texture Units

> A profile contains a **Texture Set**, which contains **Texture Units**. These are used to define a single texture to be baked using **Bake Types**.

> To the right of the image name is a suffix which is dynamically generated. You can change the suffix letters in the settings or even remove them.

> The suffix can be disabled from the addon parameters by unticking **Auto Suffix** 

> Having **multiple Texture Units** result in the Bake set **baking multiple textures** at once.



![alt text](image-16.png)


## Bake Types

> With **Bake Types** we can define what is baked from the materials that are applied to the objects in the **Bake Units**. The **Materials must utilize the Principled BSDF node** and any material which is not using this node will have to be manually converted to utilize it. **The Bake Types reflect the inputs of the Principled BSDF node** except for a few special types which are unique to the Addon.

![alt text](image-15.png)

> Each **Bake Type** has a channel selector. Note that you can select multiple channels for a Bake Type with shift+left click

![alt text](image.png)



## Special Bake types
> **Bake Types** that are not specified on the Principled BSDF node are called **Special Bake types** These generate nodes automatically during the bake which
result in the desired bake.

![alt text](image-17.png)


### Normalized Position

> This is equivalent to the **Position Bake** from substance painter using bbox as the normalization type. 

![alt text](blender_cKEJC3AEkB.webp)

> Since the axis changes depending on the platform, we have to configure the right one depending on the platform.

![alt text](image-22.webp)

![alt text](Untitled-1.webp)

> The resulting baked texture looks like the following. Each axis containing a 0 to 1 gradient using the mesh bounding box.

![alt text](gg.webp)


### Smoothness

> Basically the inverse of roughness

![alt text](blender_IEwHCECQ4m.webp)

![alt text](blender_jIAnGk8162.webp)

### Curvature

> The **pointyness** of the mesh curvature. **Mesh density** has great effect on this bake type.

![alt text](image-23.webp)

### Glossy map

> The **surface reflection** of the mesh. **Roughness** has great effect on this bake type.

![alt text](image-24.webp)

#### Light map

> The surface **brightness** and **color** from light sources

![alt text](image-25.webp)

### ColorID

> Using the user defined colors from the bake unit, we can color each bake unit to have a unique color.

![alt text](image-26.webp)

### Ambient Occlusion

> Distance calculation to the closest mesh. 

![alt text](image-27.webp)

![alt text](image-28.webp)

### Thickness
> Taken from substance painter, it's basically AO, but the rays are casted inside the mesh instead of outside.


![alt text](image-2.png)

### Normal map

> Baking normal maps is a very useful technique, either by defining a **high object** or by using a **multi resolution modifier** we can bake high detail surface imperfections to a texture.

![alt text](image-29.webp)

### World Space Normal

> Same as normal map, but it's in World space.

![alt text](image-3.png)

## Finalize

> **The last part in the pipeline** Once the bake is complete. With a single click you can create a copies of your **Bake Set** objects which now utilize only the baked textures. Great for ensuring consistency and also as a bonus makes your objects ready for exporting.

![alt text](blender_bSQVfeDZ6o.webp)


## Decals

> All Bake Units contain a single collection slot reserved for any decals.

> The Objects in this collection should be Curve Objects, Font Objects or Mesh objects

![alt text](image-20.png)

> Decals can be baked in two projection modes specified by the > _PROJ suffix on the decal object, if the projected decal doesn't work then try this.

![alt text](blender_mgCotKDYXm.webp)

> The > _PROJ  suffix should not be used with text objects

![alt text](blender_THMwXlMG2K.webp)



## Parameters

> There are various controls in the addon parameters, which need explaining.

![alt text](image-18.png)

* **Force Color Space** - a toggle which will give you an option to set the colorspace of a baked texture, manually setting this is rarely required since its automatically determined from the **Bake Types**. In certain situations you may need to control this explicitly

![alt text](blender_7L9BT6yH08.webp)


* **Toggle Console** - Whenever you bake something on Windows, a console will open up which has a visual progress bar and the option to cancel the bake with E+Ctrl

> yes it's reversed(does not currently work on non-Windows machines)

* **Auto Suffix** - Generates the suffix for the texturename from the baketypes

![alt text](blender_yslJiXpimY.webp)

> You can also manually define the suffixes from the first panel

![alt text](blender_zljkGzEKJX.webp)

* **Ignore Shape Keys** - When baking objects which utilize shape keys, you might not want to bake the distorted mesh if it is affected by stuff like AO or Decals.

![alt text](blender_WfgK9RwSqA.webp)

* **Global File Format** - Specify the texture format on a **Bake Set** basis or you can use the same file format for all **Bake Sets**.

![alt text](blender_w0jE3LHiEI.webp)

* **Decal Subdivision** - Decals are shrinkwraped around the **Low** object, this ensures that the shrinkwrapping works correctly. Some meshes require more subdiv, which can be increased on the value to the right of this tickbox.

![alt text](blender_X8PDx9mE0N.webp)

* **Use Global Decal Margin** - Just like with the margin for baking, you can specify how much margin the **Decals** have when they are baked to the UV islands on the Low object.

* **Decal Stack Height** - This is the height at which the **Decals** are shrinkwrapped to the surface of the low object, depending on the mesh resolution of the decal, this should.

* **Alpha Sensitivity** - Multiply all alpha channels by this value. Ideal for 
crisper edges when using decals. You can also manually do it in the material, but this is more convenient.









### Support

> If you find yourself stuck or if something isn't working as you intended, ask about it in the [discord channel](https://discord.gg/RvT8jKRevG)
