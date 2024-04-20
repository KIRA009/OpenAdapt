export function validateScrubbingSettings(settings: Record<string, string>) {
    const errors: Record<string, string> = {}
    if (settings.SCRUB_ENABLED) {
        return errors;
    }
    if (settings.SCRUB_CHAR.length === 0) {
        errors.SCRUB_CHAR = 'Scrubbing character is required'
    }
    if (settings.SCRUB_CHAR.length > 1) {
        errors.SCRUB_CHAR = 'Scrubbing character must be a single character'
    }
    if (settings.SCRUB_LANGUAGE.length === 0) {
        errors.SCRUB_LANGUAGE = 'Scrubbing language is required'
    }
    if (settings.SCRUB_LANGUAGE.length > 2) {
        errors.SCRUB_LANGUAGE = 'Scrubbing language must be a two character language code'
    }
    if (settings.SCRUB_FILL_COLOR.length === 0) {
        errors.SCRUB_FILL_COLOR = 'Scrubbing fill color is required'
    }

    return errors
}


export function validateRecordAndReplaySettings(settings: Record<string, string>) {
    const errors: Record<string, string> = {}
    if (settings.VIDEO_PIXEL_FORMAT.length === 0) {
        errors.VIDEO_PIXEL_FORMAT = 'Video pixel format is required'
    }
    return errors
}
