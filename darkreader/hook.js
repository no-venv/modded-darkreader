(function(){
    
    var DEFAULT_COLOUR = {
        darkScheme: {
            background: "#181a1b",
            text: "#181a1b"
        },
        lightScheme: {
            background: "#181a1b",
            text: "#181a1b"
        }
    };
    var DEFAULT__THEME = {
        mode: 1,
        brightness: 100,
        contrast: 100,
        grayscale: 0,
        sepia: 0,
        useFont: false,
        fontFamily: false
            ? "Helvetica Neue"
            : false
            ? "Segoe UI"
            : "Open Sans",
        textStroke: 0,
        engine: ThemeEngine.dynamicTheme,
        stylesheet: "",
        darkSchemeBackgroundColor: DEFAULT_COLOUR.darkScheme.background,
        darkSchemeTextColor: DEFAULT_COLOUR.darkScheme.text,
        lightSchemeBackgroundColor: DEFAULT_COLOUR.lightScheme.background,
        lightSchemeTextColor: DEFAULT_COLOUR.lightScheme.text,
        scrollbarColor: isMacOS ? "" : "auto",
        selectionColor: "auto",
        styleSystemControls: !isCSSColorSchemePropSupported,
        lightColorScheme: "Default",
        darkColorScheme: "Default",
        immediateModify: false
    };
    
    
    setTimeout(function(){
        console.log( MessageTypeUItoBG.SET_THEME)
  
        chrome.runtime.sendMessage ({
            type: MessageTypeUItoBG.SET_THEME,
            data: DEFAULT__THEME
        });

    },5000)


})();