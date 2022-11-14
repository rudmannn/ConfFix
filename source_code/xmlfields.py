def getPartialOrderFields(tag, key_before):
    fields = []
    if tag.__contains__("TextView"):
        fields = ["mSpacingAdd", "mDesiredHeightAtMeasure"]
    elif tag.__contains__("item"):
        fields = ["mLayerState.mChildren[1].mDrawable.mVectorState.mLastHWCachePixelCount",
                  "mLayerState.mChildren[1].mDrawable.mBounds.bottom",
                  "mLayerState.mChildren[1].mDrawable.mBounds.top",
                  "mLayerState.mChildren[1].mDrawable.mBounds.left",
                  "mLayerState.mChildren[1].mDrawable.mBounds.right",
                  "mLayerState.mChildren[1].mDrawable.mTmpBounds.top",
                  "mLayerState.mChildren[1].mDrawable.mTmpBounds.bottom",
                  "mLayerState.mChildren[1].mDrawable.mTmpBounds.left",
                  "mLayerState.mChildren[1].mDrawable.mTmpBounds.right"]
    return fields.__contains__(key_before)
