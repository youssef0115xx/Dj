import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import random
import tempfile
import shutil
import time

# شخصيات أقوى وأكثر تفصيلاً
personas = {
    "win10_gaming": {
        "platform": "Win32", "ua_os": "Windows NT 10.0; Win64; x64",
        "resolutions": [(1920, 1080), (2560, 1440), (3440, 1440), (3840, 2160)],
        "gpus": [
            ("Google Inc. (NVIDIA)", "ANGLE (NVIDIA, NVIDIA GeForce RTX 4090 Direct3D11 vs_5_0 ps_5_0, D3D11)"),
            ("Google Inc. (NVIDIA)", "ANGLE (NVIDIA, NVIDIA GeForce RTX 4080 Super Direct3D11 vs_5_0 ps_5_0, D3D11)"),
            ("Google Inc. (NVIDIA)", "ANGLE (NVIDIA, NVIDIA GeForce RTX 4070 Ti Direct3D11 vs_5_0 ps_5_0, D3D11)"),
            ("Google Inc. (AMD)", "ANGLE (AMD, AMD Radeon RX 7900 XTX Direct3D11 vs_5_0 ps_5_0, D3D11)"),
            ("Google Inc. (AMD)", "ANGLE (AMD, AMD Radeon RX 7800 XT Direct3D11 vs_5_0 ps_5_0, D3D11)")
        ],
        "cores": [6, 8, 12, 16, 20], "memory": [16, 32, 64]
    },
    "win11_pro": {
        "platform": "Win32", "ua_os": "Windows NT 10.0; Win64; x64",
        "resolutions": [(1920, 1080), (2560, 1440), (3840, 2160), (5120, 2880)],
        "gpus": [
            ("Google Inc. (NVIDIA)", "ANGLE (NVIDIA, NVIDIA GeForce RTX 4090 Direct3D11 vs_5_0 ps_5_0, D3D11)"),
            ("Google Inc. (Intel)", "ANGLE (Intel, Intel(R) Arc A770 Direct3D11 vs_5_0 ps_5_0, D3D11)")
        ],
        "cores": [8, 12, 16, 24], "memory": [32, 64, 128]
    },
    "mac_studio": {
        "platform": "MacIntel", "ua_os": "Macintosh; Intel Mac OS X 10_15_7",
        "resolutions": [(2560, 1600), (3024, 1964), (3456, 2234), (5120, 2880)],
        "gpus": [
            ("Google Inc. (Apple)", "ANGLE (Apple, Apple M2 Ultra, OpenGL 4.1)"),
            ("Google Inc. (Apple)", "ANGLE (Apple, Apple M2 Max, OpenGL 4.1)"),
            ("Google Inc. (Apple)", "ANGLE (Apple, Apple M1 Ultra, OpenGL 4.1)")
        ],
        "cores": [10, 12, 16, 20, 24], "memory": [32, 64, 128]
    },
    "mac_pro": {
        "platform": "MacIntel", "ua_os": "Macintosh; Intel Mac OS X 10_15_7", 
        "resolutions": [(2880, 1800), (3024, 1964), (5120, 2880), (6016, 3384)],
        "gpus": [("Google Inc. (Apple)", "ANGLE (Apple, Apple M2 Ultra, OpenGL 4.1)")],
        "cores": [16, 20, 24], "memory": [64, 128, 192]
    }
}

# اختيار شخصية قوية
os_weights = [30, 35, 20, 15]  # توزيع احتمالي واقعي
os_type = random.choices(list(personas.keys()), weights=os_weights)[0]
persona = personas[os_type]
width, height = random.choice(persona["resolutions"])
gpu_vendor, gpu_renderer = random.choice(persona["gpus"])
cores = random.choice(persona["cores"])
memory = random.choice(persona["memory"])

# Chrome version أكثر واقعية
chrome_versions = ["128.0.6613.84", "128.0.6613.85", "128.0.6613.86", "129.0.6668.58", "129.0.6668.59"]
chrome_ver = random.choice(chrome_versions)
ua = f"Mozilla/5.0 ({persona['ua_os']}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Safari/537.36"

# لغات ومناطق زمنية متنوعة
languages = ["en-US,en;q=0.9", "en-GB,en;q=0.9", "ar-EG,ar;q=0.9,en;q=0.8", "de-DE,de;q=0.9,en;q=0.8", "fr-FR,fr;q=0.9,en;q=0.8"]
timezones = ["America/New_York", "Europe/London", "Europe/Berlin", "America/Los_Angeles", "Asia/Tokyo", "Africa/Cairo"]
language = random.choice(languages)
timezone = random.choice(timezones)

# معلومات إضافية للتمويه القوي
connection_rtt = random.randint(20, 250)
connection_downlink = round(random.uniform(5.0, 100.0), 1)
connection_type = random.choice(['4g', '4g', '4g', '5g', 'wifi'])
battery_level = round(random.uniform(0.15, 0.95), 2)
battery_charging = random.choice([True, False, False])
touch_points = 0 if "mac" in os_type else random.choice([0, 0, 0, 5, 10])

# إعداد Chrome قوي
profile_dir = tempfile.mkdtemp(prefix="ultra_stealth_")
options = Options()
options.add_argument(f"--user-data-dir={profile_dir}")
options.add_argument(f"--user-agent={ua}")
options.add_argument(f"--window-size={width},{height}")
options.add_argument(f"--lang={language.split(',')[0]}")

# Arguments قوية للتمويه الفائق
ultra_stealth_args = [
    "--disable-blink-features=AutomationControlled",
    "--disable-infobars", "--disable-extensions", "--no-first-run", "--disable-dev-shm-usage",
    "--disable-client-side-phishing-detection", "--disable-component-update", "--disable-default-apps",
    "--disable-domain-reliability", "--disable-features=TranslateUI,BlinkGenPropertyTrees,VizDisplayCompositor",
    "--disable-hang-monitor", "--disable-sync", "--disable-web-security", "--no-crash-upload",
    "--disable-background-timer-throttling", "--disable-backgrounding-occluded-windows",
    "--disable-renderer-backgrounding", "--disable-field-trial-config", "--disable-ipc-flooding-protection",
    "--enable-features=NetworkService,NetworkServiceLogging", "--force-color-profile=srgb",
    "--metrics-recording-only", "--no-report-upload", "--use-mock-keychain",
    "--disable-component-extensions-with-background-pages", "--disable-extensions-file-access-check",
    "--disable-extensions-http-throttling", "--disable-prompt-on-repost"
]

for arg in ultra_stealth_args:
    options.add_argument(arg)

options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging", "enable-blink-features"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", {
    "credentials_enable_service": False, "profile.password_manager_enabled": False,
    "profile.default_content_setting_values.notifications": 2,
    "profile.default_content_setting_values.geolocation": 2,
    "profile.default_content_setting_values.media_stream": 2,
    "webrtc.ip_handling_policy": "disable_non_proxied_udp",
    "webrtc.multiple_routes_enabled": False, "webrtc.nonproxied_udp_enabled": False,
    "profile.block_third_party_cookies": False, "profile.cookie_controls_mode": 0,
    "dns_prefetching.enabled": True, "alternate_error_pages.enabled": False
})

# إنشاء المتصفح الفائق
driver = uc.Chrome(options=options, use_subprocess=True)

# CDP إعدادات قوية
driver.execute_cdp_cmd('Emulation.setTimezoneOverride', {'timezoneId': timezone})
driver.execute_cdp_cmd('Network.setExtraHTTPHeaders', {'headers': {
    'Accept-Language': language,
    'Sec-CH-UA': f'"Google Chrome";v="{chrome_ver.split(".")[0]}", "Chromium";v="{chrome_ver.split(".")[0]}", "Not=A?Brand";v="24"',
    'Sec-CH-UA-Mobile': '?0', 'Sec-CH-UA-Platform': f'"{persona["platform"]}"',
    'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-User': '?1'
}})

driver.execute_cdp_cmd('Network.setUserAgentOverride', {
    'userAgent': ua, 'acceptLanguage': language, 'platform': persona['platform']
})

# محاكاة شبكة واقعية
driver.execute_cdp_cmd('Network.emulateNetworkConditions', {
    'offline': False, 'latency': connection_rtt, 
    'downloadThroughput': int(connection_downlink * 1000000),
    'uploadThroughput': int(connection_downlink * 500000)
})

# السكريبت الفائق الأقوى على الإطلاق
mega_stealth_script = f"""
// === WebGL التمويه الأقوى ===
const getParam = WebGLRenderingContext.prototype.getParameter;
const getExt = WebGLRenderingContext.prototype.getExtension;
const getSuppExt = WebGLRenderingContext.prototype.getSupportedExtensions;

WebGLRenderingContext.prototype.getParameter = function(p) {{
    const fakeParams = {{
        37445: '{gpu_vendor}', 37446: '{gpu_renderer}', 3379: 16384, 34076: 16384,
        34024: 32, 34930: 32, 35071: 64, 36347: 4096, 36348: 4096, 36349: 1024,
        3386: new Int32Array([1, 1024]), 33902: new Float32Array([1.0, 1024.0]),
        35660: 32, 35661: 32, 36063: 16384
    }};
    return fakeParams[p] || getParam.apply(this, arguments);
}};

WebGLRenderingContext.prototype.getExtension = function(name) {{
    const allowed = ['WEBGL_debug_renderer_info', 'EXT_texture_filter_anisotropic', 'WEBKIT_EXT_texture_filter_anisotropic', 
                    'MOZ_EXT_texture_filter_anisotropic', 'WEBGL_compressed_texture_s3tc', 'WEBGL_depth_texture',
                    'OES_element_index_uint', 'OES_standard_derivatives', 'OES_vertex_array_object', 'WEBGL_lose_context'];
    return allowed.includes(name) ? getExt.apply(this, arguments) : null;
}};

WebGLRenderingContext.prototype.getSupportedExtensions = function() {{
    return ['WEBGL_debug_renderer_info', 'EXT_texture_filter_anisotropic', 'WEBGL_compressed_texture_s3tc'];
}};

// === Canvas التمويه المتطور ===
const origToDataURL = HTMLCanvasElement.prototype.toDataURL;
const origGetImageData = CanvasRenderingContext2D.prototype.getImageData;

function addAdvancedNoise(imageData) {{
    const data = imageData.data;
    const noiseLevel = {random.randint(1, 4)};
    for (let i = 0; i < data.length; i += 4) {{
        if (Math.random() < 0.08) {{
            const noise = Math.floor(Math.random() * noiseLevel * 2) - noiseLevel;
            data[i] = Math.max(0, Math.min(255, data[i] + noise));
            data[i + 1] = Math.max(0, Math.min(255, data[i + 1] + noise));
            data[i + 2] = Math.max(0, Math.min(255, data[i + 2] + noise));
        }}
    }}
    return imageData;
}}

HTMLCanvasElement.prototype.toDataURL = function() {{
    const ctx = this.getContext('2d');
    if (ctx) {{
        const imgData = ctx.getImageData(0, 0, this.width, this.height);
        ctx.putImageData(addAdvancedNoise(imgData), 0, 0);
    }}
    return origToDataURL.apply(this, arguments);
}};

CanvasRenderingContext2D.prototype.getImageData = function() {{
    return addAdvancedNoise(origGetImageData.apply(this, arguments));
}};

// === Navigator التمويه الشامل ===
const descriptors = {{
    webdriver: {{get: () => undefined}}, platform: {{get: () => '{persona["platform"]}'}},
    hardwareConcurrency: {{get: () => {cores}}}, deviceMemory: {{get: () => {memory}}},
    maxTouchPoints: {{get: () => {touch_points}}},
    languages: {{get: () => ['{language.split(",")[0]}', 'en']}},
    cookieEnabled: {{get: () => true}}, doNotTrack: {{get: () => null}},
    onLine: {{get: () => true}}
}};
Object.keys(descriptors).forEach(key => Object.defineProperty(navigator, key, descriptors[key]));

// === Audio Context التمويه القوي ===
['AudioContext', 'webkitAudioContext'].forEach(name => {{
    if (window[name]) {{
        const origCreateAnalyser = window[name].prototype.createAnalyser;
        const origCreateOscillator = window[name].prototype.createOscillator;
        
        window[name].prototype.createAnalyser = function() {{
            const analyser = origCreateAnalyser.apply(this);
            const origGetFloat = analyser.getFloatFrequencyData;
            analyser.getFloatFrequencyData = function(array) {{
                origGetFloat.apply(this, arguments);
                for (let i = 0; i < array.length; i++) array[i] += (Math.random() - 0.5) * 0.001;
            }};
            return analyser;
        }};
        
        window[name].prototype.createOscillator = function() {{
            const osc = origCreateOscillator.apply(this);
            const origFreq = Object.getOwnPropertyDescriptor(OscillatorNode.prototype, 'frequency');
            Object.defineProperty(osc, 'frequency', {{
                get: function() {{
                    const freq = origFreq.get.apply(this);
                    freq.value += (Math.random() - 0.5) * 0.1;
                    return freq;
                }}
            }});
            return osc;
        }};
    }}
}});

// === إزالة متغيرات الأتمتة الشاملة ===
const automationVars = ['cdc_adoQpoasnfa76pfcZLmcfl_Array', 'cdc_adoQpoasnfa76pfcZLmcfl_Promise', 
                       'cdc_adoQpoasnfa76pfcZLmcfl_Symbol', 'cdc_adoQpoasnfa76pfcZLmcfl_JSON',
                       'cdc_adoQpoasnfa76pfcZLmcfl_Object', 'cdc_adoQpoasnfa76pfcZLmcfl_Proxy'];
automationVars.forEach(v => delete window[v]);

Object.keys(window).forEach(key => {{
    if (key.includes('cdc_') || key.includes('automation') || key.includes('webdriver')) delete window[key];
}});

// === Screen التمويه الدقيق ===
const screenProps = {{
    width: {{get: () => {width}}}, height: {{get: () => {height}}},
    availWidth: {{get: () => {width}}}, availHeight: {{get: () => {height - random.randint(40, 80)}}},
    colorDepth: {{get: () => 24}}, pixelDepth: {{get: () => 24}}
}};
Object.keys(screenProps).forEach(key => Object.defineProperty(screen, key, screenProps[key]));

// === Font Fingerprinting التمويه ===
const origOffsetWidth = Object.getOwnPropertyDescriptor(HTMLElement.prototype, 'offsetWidth');
const origOffsetHeight = Object.getOwnPropertyDescriptor(HTMLElement.prototype, 'offsetHeight');

Object.defineProperty(HTMLElement.prototype, 'offsetWidth', {{
    get: function() {{
        const w = origOffsetWidth.get.apply(this);
        return w + (Math.random() < 0.05 ? (Math.random() > 0.5 ? 1 : -1) : 0);
    }}
}});

Object.defineProperty(HTMLElement.prototype, 'offsetHeight', {{
    get: function() {{
        const h = origOffsetHeight.get.apply(this);
        return h + (Math.random() < 0.05 ? (Math.random() > 0.5 ? 1 : -1) : 0);
    }}
}});

// === Performance API التمويه ===
if (window.performance?.now) {{
    const origNow = window.performance.now;
    const timeOffset = Math.random() * 2000;
    window.performance.now = function() {{ return origNow.apply(this) + timeOffset; }};
}}

// === Battery API التمويه المتقدم ===
if (navigator.getBattery) {{
    const origGetBattery = navigator.getBattery;
    navigator.getBattery = function() {{
        return origGetBattery.apply(this).then(battery => {{
            Object.defineProperties(battery, {{
                level: {{get: () => {battery_level}}}, charging: {{get: () => {str(battery_charging).lower()}}},
                chargingTime: {{get: () => {random.randint(3600, 7200) if battery_charging else "Infinity"}}},
                dischargingTime: {{get: () => {random.randint(7200, 28800) if not battery_charging else "Infinity"}}}
            }});
            return battery;
        }});
    }};
}}

// === Connection API التمويه ===
if (navigator.connection) {{
    Object.defineProperties(navigator.connection, {{
        rtt: {{get: () => {connection_rtt}}}, downlink: {{get: () => {connection_downlink}}},
        effectiveType: {{get: () => '{connection_type}'}}, saveData: {{get: () => false}}
    }});
}}

// === Date وTimezone التمويه ===
const origGetTimezoneOffset = Date.prototype.getTimezoneOffset;
Date.prototype.getTimezoneOffset = function() {{ return {random.randint(-720, 720)}; }};

if (window.Intl?.DateTimeFormat) {{
    const origResolvedOptions = Intl.DateTimeFormat.prototype.resolvedOptions;
    Intl.DateTimeFormat.prototype.resolvedOptions = function() {{
        const opts = origResolvedOptions.apply(this, arguments);
        opts.timeZone = '{timezone}';
        return opts;
    }};
}}

// === إخفاء iframe وWindow properties ===
Object.defineProperties(window, {{
    top: {{get: () => window}}, parent: {{get: () => window}}, frameElement: {{get: () => null}}
}});

// === Chrome Runtime إخفاء ===
if (window.chrome?.runtime) {{
    ['onConnect', 'onMessage', 'sendMessage'].forEach(prop => delete window.chrome.runtime[prop]);
}}

// === Mouse Events محاكاة ===
let mouseX = Math.random() * {width}, mouseY = Math.random() * {height};
setInterval(() => {{
    mouseX += (Math.random() - 0.5) * 10;
    mouseY += (Math.random() - 0.5) * 10;
    mouseX = Math.max(0, Math.min({width}, mouseX));
    mouseY = Math.max(0, Math.min({height}, mouseY));
    
    const event = new MouseEvent('mousemove', {{
        clientX: mouseX, clientY: mouseY, bubbles: true
    }});
    document.dispatchEvent(event);
}}, Math.random() * 5000 + 2000);

// === Permissions API تمويه ===
if (navigator.permissions?.query) {{
    const origQuery = navigator.permissions.query;
    navigator.permissions.query = function(obj) {{
        return origQuery.apply(this, arguments).then(result => {{
            if (obj.name === 'notifications') result.state = 'denied';
            return result;
        }});
    }};
}}
"""

# حقن السكريبت الفائق
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': mega_stealth_script})

# التنقل مع سلوك بشري متقدم
driver.get("https://bot.sannysoft.com/")
time.sleep(random.uniform(4, 8))

# محاكاة سلوك بشري متقدم
for i in range(random.randint(3, 6)):
    scroll_amount = random.randint(150, 400)
    driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
    time.sleep(random.uniform(1.5, 3.5))

# نقرات عشوائية
driver.execute_script("""
    setTimeout(() => {
        const elements = document.querySelectorAll('div, span, p');
        const randomEl = elements[Math.floor(Math.random() * elements.length)];
        if (randomEl) randomEl.click();
    }, """ + str(random.randint(2000, 5000)) + """);
""")

print("✅ متصفح فائق القوة جاهز! القوة: 10/10")
input("اضغط Enter للإغلاق...")

driver.quit()
shutil.rmtree(profile_dir)