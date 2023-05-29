import random

def getEnumAttributes(tag):
    if tag.__contains__("TextView"):
        return ["{http://schemas.android.com/apk/res/android}textAppearance",
                "{http://schemas.android.com/apk/res/android}hint",
                "{http://schemas.android.com/apk/res/android}text",
                "{http://schemas.android.com/apk/res/android}editorExtras",
                "{http://schemas.android.com/apk/res/android}textCursorDrawable",
                "{http://schemas.android.com/apk/res/android}textSelectHandleLeft",
                "{http://schemas.android.com/apk/res/android}textSelectHandleRight",
                "{http://schemas.android.com/apk/res/android}textSelectHandle",
                "{http://schemas.android.com/apk/res/android}textEditSuggestionItemLayout",
                "{http://schemas.android.com/apk/res/android}textEditSuggestionHighlightStyle",
                "{http://schemas.android.com/apk/res/android}autoSizePresetSizes",
                "{http://schemas.android.com/apk/res/android}textAppearance"
                ]

def getResourceIdAttributes(tag):
    if tag.__contains__("TextView"):
        return ["{http://schemas.android.com/apk/res/android}textAppearance",
                "{http://schemas.android.com/apk/res/android}hint",
                "{http://schemas.android.com/apk/res/android}text",
                "{http://schemas.android.com/apk/res/android}editorExtras",
                "{http://schemas.android.com/apk/res/android}textCursorDrawable",
                "{http://schemas.android.com/apk/res/android}textSelectHandleLeft",
                "{http://schemas.android.com/apk/res/android}textSelectHandleRight",
                "{http://schemas.android.com/apk/res/android}textSelectHandle",
                "{http://schemas.android.com/apk/res/android}textEditSuggestionItemLayout",
                "{http://schemas.android.com/apk/res/android}textEditSuggestionHighlightStyle",
                "{http://schemas.android.com/apk/res/android}autoSizePresetSizes",
                "{http://schemas.android.com/apk/res/android}textAppearance"
                ]
    # elif tag.__contains__("item"):
    #     return ["{http://schemas.android.com/apk/res/android}top",
    #             "{http://schemas.android.com/apk/res/android}bottom",
    #             "{http://schemas.android.com/apk/res/android}left",
    #             "{http://schemas.android.com/apk/res/android}right"
    #             ]


def getDimensionalAttributes(tag):
    if tag == "LayoutParam":
        return [
                "{http://schemas.android.com/apk/res/android}layout_width",
                "{http://schemas.android.com/apk/res/android}layout_marginHorizontal",
                "{http://schemas.android.com/apk/res/android}layout_marginVertical",
                "{http://schemas.android.com/apk/res/android}layout_marginLeft",
                "{http://schemas.android.com/apk/res/android}layout_marginRight",
                "{http://schemas.android.com/apk/res/android}layout_marginTop",
                "{http://schemas.android.com/apk/res/android}layout_marginBottom",
                "{http://schemas.android.com/apk/res/android}layout_marginStart",
                "{http://schemas.android.com/apk/res/android}layout_marginEnd",
                "{http://schemas.android.com/apk/res/android}layout_margin"
                ]
    elif tag.__contains__("TextView"):
        arr = [
            "{http://schemas.android.com/apk/res-auto}lineHeight",
                "{http://schemas.android.com/apk/res/android}lineSpacingExtra",
                "{http://schemas.android.com/apk/res/android}height",
                "{http://schemas.android.com/apk/res/android}firstBaselineToTopHeight",
                "{http://schemas.android.com/apk/res/android}lastBaselineToBottomHeight",
                "{http://schemas.android.com/apk/res/android}drawablePadding",
                "{http://schemas.android.com/apk/res/android}width",
                "{http://schemas.android.com/apk/res/android}minHeight",
                "{http://schemas.android.com/apk/res/android}maxHeight",
                "{http://schemas.android.com/apk/res/android}minWidth",
                "{http://schemas.android.com/apk/res/android}maxWidth",
                "{http://schemas.android.com/apk/res/android}autoSizeStepGranularity",
                "{http://schemas.android.com/apk/res/android}autoSizeMinTextSize",
                "{http://schemas.android.com/apk/res/android}autoSizeMaxTextSize",
                ]
        random.shuffle(arr)
        return arr

        # return [
        #         "{http://schemas.android.com/apk/res/android}layout_marginHorizontal",
        #         "{http://schemas.android.com/apk/res/android}layout_marginVertical",
        #         "{http://schemas.android.com/apk/res/android}layout_marginLeft",
        #         "{http://schemas.android.com/apk/res/android}layout_marginRight",
        #         "{http://schemas.android.com/apk/res/android}layout_marginTop",
        #         "{http://schemas.android.com/apk/res/android}layout_marginBottom",
        #         "{http://schemas.android.com/apk/res/android}layout_marginStart",
        #         "{http://schemas.android.com/apk/res/android}layout_marginEnd",
        #         "{http://schemas.android.com/apk/res/android}layout_margin"
        #         ]
    elif str(tag) == "View":
        return [
            # "{http://schemas.android.com/apk/res/android}paddingHorizontal",
            # "{http://schemas.android.com/apk/res/android}paddingVertical",
            "{http://schemas.android.com/apk/res/android}paddingLeft",
            "{http://schemas.android.com/apk/res/android}paddingRight",
            "{http://schemas.android.com/apk/res/android}paddingTop",
            "{http://schemas.android.com/apk/res/android}paddingBottom",
            "{http://schemas.android.com/apk/res/android}padding",
            # "{http://schemas.android.com/apk/res/android}paddingStart",
            # "{http://schemas.android.com/apk/res/android}paddingEnd",
            "{http://schemas.android.com/apk/res/android}minWidth",
            "{http://schemas.android.com/apk/res/android}minHeight",
            "{http://schemas.android.com/apk/res/android}scrollbarSize"
        ]
    elif tag.__contains__("item"):
        return ["{http://schemas.android.com/apk/res/android}top",
                "{http://schemas.android.com/apk/res/android}bottom",
                "{http://schemas.android.com/apk/res/android}left",
                "{http://schemas.android.com/apk/res/android}right"]


def getStringAttributes(tag):
    if tag.__contains__("TextView"):
        return ["{http://schemas.android.com/apk/res/android}privateImeOptions",
                "{http://schemas.android.com/apk/res/android}textLocale",
                "{http://schemas.android.com/apk/res/android}fontFamily",
                "{http://schemas.android.com/apk/res/android}fontFeatureSettings",
                "{http://schemas.android.com/apk/res/android}fontVariationSettings",
                "{http://schemas.android.com/apk/res/android}inputMethod",
                "{http://schemas.android.com/apk/res/android}digits",
                "{http://schemas.android.com/apk/res/android}hint",
                "{http://schemas.android.com/apk/res/android}text",
                "{http://schemas.android.com/apk/res/android}imeActionLabel",
                "{http://schemas.android.com/apk/res/android}fontVariationSettings",
                ]

def getIntAttributes(tag):
    if tag.__contains__("TextView"):
        return ["{http://schemas.android.com/apk/res/android}lines",
                "{http://schemas.android.com/apk/res/android}minLines",
                "{http://schemas.android.com/apk/res/android}textFontWeight",
                "{http://schemas.android.com/apk/res/android}maxEms"]


def getFloatAttributes(tag):
    if tag.__contains__("TextView"):
        return ["{http://schemas.android.com/apk/res/android}textScaleX",
                "{http://schemas.android.com/apk/res/android}lineSpacingMultiplier",
                "{http://schemas.android.com/apk/res/android}shadowDx",
                "{http://schemas.android.com/apk/res/android}shadowDy",
                "{http://schemas.android.com/apk/res/android}shadowRadius"]


def getBooleanAttributes(tag):
    if tag.__contains__("TextView"):
        return ["{http://schemas.android.com/apk/res/android}editable",
                "{http://schemas.android.com/apk/res/android}phoneNumber",
                "{http://schemas.android.com/apk/res/android}autoText",
                "{http://schemas.android.com/apk/res/android}linksClickable",
                "{http://schemas.android.com/apk/res/android}includeFontPadding",
                "{http://schemas.android.com/apk/res/android}cursorVisible",
                "{http://schemas.android.com/apk/res/android}freezesText",
                "{http://schemas.android.com/apk/res/android}enabled",
                "{http://schemas.android.com/apk/res/android}password",
                "{http://schemas.android.com/apk/res/android}allowUndo",
                "{http://schemas.android.com/apk/res/android}textIsSelectable",
                "{http://schemas.android.com/apk/res/android}clickable",
                "{http://schemas.android.com/apk/res/android}longClickable",
                "{http://schemas.android.com/apk/res/android}textAllCaps",
                "{http://schemas.android.com/apk/res/android}elegantTextHeight",
                "{http://schemas.android.com/apk/res/android}fallbackLineSpacing"
                ]


def getColorAttributes(tag):
    if tag.__contains__("TextView"):
        arr = [ "{http://schemas.android.com/apk/res/android}textColor",
                "{http://schemas.android.com/apk/res-auto}drawableTint",
                "{http://schemas.android.com/apk/res/android}textColorHighlight",
                "{http://schemas.android.com/apk/res/android}textColorHint",
                "{http://schemas.android.com/apk/res/android}textColorLink",
                # "{http://schemas.android.com/apk/res/android}drawableTint",
                ]
        random.shuffle(arr)
        return arr
    elif tag == "CompoundButton":
        arr = ["{http://schemas.android.com/apk/res-auto}buttonTint"]
        random.shuffle(arr)
        return arr
    return []


def getDrawableAttributes(tag):
    if tag == "View":
        return ["{http://schemas.android.com/apk/res-android}scrollbarTrackHorizontal",
                "{http://schemas.android.com/apk/res/android}scrollbarThumbHorizontal",
                "{http://schemas.android.com/apk/res/android}scrollbarTrackVertical",
                "{http://schemas.android.com/apk/res/android}scrollbarThumbVertical",
                "{http://schemas.android.com/apk/res/android}background"
                ]
    elif tag.__contains__("TextView"):
        ret = ["{http://schemas.android.com/apk/res-auto}drawableStartCompat",
                "{http://schemas.android.com/apk/res/android}drawableLeft",
                "{http://schemas.android.com/apk/res-auto}drawableLeftCompat",
                "{http://schemas.android.com/apk/res/android}drawableRight",
                "{http://schemas.android.com/apk/res/android}drawableTop",
                "{http://schemas.android.com/apk/res/android}drawableBottom",
                "{http://schemas.android.com/apk/res/android}drawableStart",
                "{http://schemas.android.com/apk/res-auto}drawableTopCompat",
                "{http://schemas.android.com/apk/res-auto}drawableBottomCompat",
                "{http://schemas.android.com/apk/res-auto}drawableRightCompat",
                "{http://schemas.android.com/apk/res-auto}drawableEndCompat"
                ]
        random.shuffle(ret)
        return ret

    elif tag.__contains__("ImageView") or tag.__contains__("ImageButton") or \
            tag.__contains__("FloatingActionButton"):
        return [
            "{http://schemas.android.com/apk/res/android}src",
            "{http://schemas.android.com/apk/res-auto}srcCompat"]
    return []
