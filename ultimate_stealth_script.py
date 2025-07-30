import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import random
import tempfile
import shutil
import time

personas = {
    "win11_gaming_elite": {
        "platform": "Win32", "ua_os": "Windows NT 10.0; Win64; x64",
        "resolutions": [(2560, 1440), (3440, 1440), (3840, 2160), (5120, 2880)],
        "gpus": [
            ("Google Inc. (NVIDIA)", "ANGLE (NVIDIA, NVIDIA GeForce RTX 4090 Direct3D11 vs_5_0 ps_5_0, D3D11)"),
            ("Google Inc. (NVIDIA)", "ANGLE (NVIDIA, NVIDIA GeForce RTX 4080 Super Direct3D11 vs_5_0 ps_5_0, D3D11)"),
            ("Google Inc. (AMD)", "ANGLE (AMD, AMD Radeon RX 7900 XTX Direct3D11 vs_5_0 ps_5_0, D3D11)")
        ],
        "cores": [12, 16, 20, 24], "memory": [32, 64, 128],
        "gpu_memory": [16384, 24576], "cpu_cache": [64, 128],
        "ram_speed": [4000, 5200, 6000]
    },
    "mac_studio_ultra": {
        "platform": "MacIntel", "ua_os": "Macintosh; Intel Mac OS X 10_15_7",
        "resolutions": [(3024, 1964), (3456, 2234), (5120, 2880), (6016, 3384)],
        "gpus": [
            ("Google Inc. (Apple)", "ANGLE (Apple, Apple M2 Ultra, OpenGL 4.1)"),
            ("Google Inc. (Apple)", "ANGLE (Apple, Apple M2 Max, OpenGL 4.1)")
        ],
        "cores": [16, 20, 24], "memory": [64, 128, 192],
        "gpu_memory": [8192, 12288], "cpu_cache": [64, 128],
        "ram_speed": [6400, 8000]
    },
    "linux_workstation": {
        "platform": "Linux x86_64", "ua_os": "X11; Linux x86_64",
        "resolutions": [(1920, 1080), (2560, 1440), (3840, 2160)],
        "gpus": [
            ("Google Inc. (NVIDIA)", "ANGLE (NVIDIA, NVIDIA GeForce RTX 4070 Ti Direct3D11 vs_5_0 ps_5_0, D3D11)"),
            ("Google Inc. (AMD)", "ANGLE (AMD, AMD Radeon RX 7800 XT Direct3D11 vs_5_0 ps_5_0, D3D11)")
        ],
        "cores": [8, 12, 16], "memory": [32, 64],
        "gpu_memory": [8192, 12288], "cpu_cache": [32, 64],
        "ram_speed": [3200, 3600, 4000]
    }
}

os_weights = [40, 35, 25]
os_type = random.choices(list(personas.keys()), weights=os_weights)[0]
persona = personas[os_type]

width, height = random.choice(persona["resolutions"])
gpu_vendor, gpu_renderer = random.choice(persona["gpus"])
cores = random.choice(persona["cores"])
memory = random.choice(persona["memory"])
gpu_memory = random.choice(persona["gpu_memory"])
cpu_cache = random.choice(persona["cpu_cache"])
ram_speed = random.choice(persona["ram_speed"])

chrome_versions = ["129.0.6668.58", "129.0.6668.59", "129.0.6668.60", "130.0.6712.0", "130.0.6712.1"]
chrome_ver = random.choice(chrome_versions)
ua = f"Mozilla/5.0 ({persona['ua_os']}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Safari/537.36"

network_profiles = {
    "home_wifi": {
        "latency": (10, 50), "jitter": (2, 10), "packet_loss": (0.001, 0.01),
        "downlink": (50, 200), "uplink": (20, 100)
    },
    "mobile_5g": {
        "latency": (20, 80), "jitter": (5, 15), "packet_loss": (0.005, 0.02),
        "downlink": (100, 500), "uplink": (50, 200)
    },
    "office_fiber": {
        "latency": (5, 20), "jitter": (1, 5), "packet_loss": (0.0001, 0.001),
        "downlink": (200, 1000), "uplink": (100, 500)
    }
}

network_type = random.choice(list(network_profiles.keys()))
network_config = network_profiles[network_type]

connection_rtt = random.randint(network_config["latency"][0], network_config["latency"][1])
connection_downlink = round(random.uniform(network_config["downlink"][0], network_config["downlink"][1]), 1)
connection_uplink = round(random.uniform(network_config["uplink"][0], network_config["uplink"][1]), 1)
connection_type = random.choice(['4g', '4g', '4g', '5g', 'wifi', 'wifi'])

battery_level = round(random.uniform(0.15, 0.95), 2)
battery_charging = random.choice([True, False, False])
battery_charging_time = random.randint(3600, 7200) if battery_charging else 0
battery_discharging_time = random.randint(7200, 28800) if not battery_charging else float('inf')

geolocation_profiles = {
    "new_york": {"lat": 40.7128, "lng": -74.0060, "accuracy": (10, 50)},
    "london": {"lat": 51.5074, "lng": -0.1278, "accuracy": (10, 50)},
    "tokyo": {"lat": 35.6762, "lng": 139.6503, "accuracy": (10, 50)},
    "berlin": {"lat": 52.5200, "lng": 13.4050, "accuracy": (10, 50)}
}

location_profile = random.choice(list(geolocation_profiles.keys()))
location_config = geolocation_profiles[location_profile]

language_profiles = {
    "en_US": {"lang": "en-US,en;q=0.9", "timezone": "America/New_York"},
    "en_GB": {"lang": "en-GB,en;q=0.9", "timezone": "Europe/London"},
    "de_DE": {"lang": "de-DE,de;q=0.9,en;q=0.8", "timezone": "Europe/Berlin"},
    "ja_JP": {"lang": "ja-JP,ja;q=0.9,en;q=0.8", "timezone": "Asia/Tokyo"}
}

lang_profile = random.choice(list(language_profiles.keys()))
language = language_profiles[lang_profile]["lang"]
timezone = language_profiles[lang_profile]["timezone"]

profile_dir = tempfile.mkdtemp(prefix="ultimate_stealth_")
options = Options()
options.add_argument(f"--user-data-dir={profile_dir}")
options.add_argument(f"--user-agent={ua}")
options.add_argument(f"--window-size={width},{height}")
options.add_argument(f"--lang={language.split(',')[0]}")

ultimate_stealth_args = [
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
    "--disable-extensions-http-throttling", "--disable-prompt-on-repost",
    "--disable-webgl", "--disable-webgl2", "--disable-3d-apis",
    "--disable-gpu-sandbox", "--disable-software-rasterizer",
    "--disable-background-networking", "--disable-default-apps",
    "--disable-sync-preferences", "--disable-translate",
    "--disable-web-resources", "--disable-plugins-discovery",
    "--disable-preconnect", "--disable-prefetch",
    "--disable-background-downloads", "--disable-background-upload"
]

for arg in ultimate_stealth_args:
    options.add_argument(arg)

advanced_prefs = {
    "credentials_enable_service": False, "profile.password_manager_enabled": False,
    "profile.default_content_setting_values.notifications": 2,
    "profile.default_content_setting_values.geolocation": 2,
    "profile.default_content_setting_values.media_stream": 2,
    "webrtc.ip_handling_policy": "disable_non_proxied_udp",
    "webrtc.multiple_routes_enabled": False, "webrtc.nonproxied_udp_enabled": False,
    "profile.block_third_party_cookies": False, "profile.cookie_controls_mode": 0,
    "dns_prefetching.enabled": True, "alternate_error_pages.enabled": False,
    "profile.default_content_setting_values.camera": 2,
    "profile.default_content_setting_values.microphone": 2,
    "profile.default_content_setting_values.clipboard": 2,
    "profile.default_content_setting_values.mixed_script": 1,
    "profile.default_content_setting_values.media_stream_mic": 2,
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.protocol_handlers": 2,
    "profile.default_content_setting_values.ppapi_broker": 2,
    "profile.default_content_setting_values.automatic_downloads": 1,
    "profile.default_content_setting_values.midi_sysex": 2,
    "profile.default_content_setting_values.push_messaging": 2,
    "profile.default_content_setting_values.durable_storage": 2
}

options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging", "enable-blink-features"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", advanced_prefs)

driver = uc.Chrome(options=options, use_subprocess=True)

driver.execute_cdp_cmd('Emulation.setTimezoneOverride', {'timezoneId': timezone})
driver.execute_cdp_cmd('Network.setExtraHTTPHeaders', {'headers': {
    'Accept-Language': language,
    'Sec-CH-UA': f'"Google Chrome";v="{chrome_ver.split(".")[0]}", "Chromium";v="{chrome_ver.split(".")[0]}", "Not=A?Brand";v="24"',
    'Sec-CH-UA-Mobile': '?0', 'Sec-CH-UA-Platform': f'"{persona["platform"]}"',
    'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-User': '?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br', 'Cache-Control': 'max-age=0'
}})

driver.execute_cdp_cmd('Network.setUserAgentOverride', {
    'userAgent': ua, 'acceptLanguage': language, 'platform': persona['platform']
})

driver.execute_cdp_cmd('Network.emulateNetworkConditions', {
    'offline': False, 'latency': connection_rtt, 
    'downloadThroughput': int(connection_downlink * 1000000),
    'uploadThroughput': int(connection_uplink * 1000000),
    'packetLoss': random.uniform(network_config["packet_loss"][0], network_config["packet_loss"][1])
})

ultimate_stealth_script = f"""
const getParam = WebGLRenderingContext.prototype.getParameter;
const getExt = WebGLRenderingContext.prototype.getExtension;
const getSuppExt = WebGLRenderingContext.prototype.getSupportedExtensions;

WebGLRenderingContext.prototype.getParameter = function(p) {{
    const fakeParams = {{
        37445: '{gpu_vendor}', 37446: '{gpu_renderer}', 3379: 16384, 34076: 16384,
        34024: 32, 34930: 32, 35071: 64, 36347: 4096, 36348: 4096, 36349: 1024,
        3386: new Int32Array([1, 1024]), 33902: new Float32Array([1.0, 1024.0]),
        35660: 32, 35661: 32, 36063: 16384, 37446: '{gpu_renderer}',
        37445: '{gpu_vendor}', 37447: 4096, 37448: 4096, 37449: 1024
    }};
    return fakeParams[p] || getParam.apply(this, arguments);
}};

WebGLRenderingContext.prototype.getExtension = function(name) {{
    const allowed = ['WEBGL_debug_renderer_info', 'EXT_texture_filter_anisotropic', 
                    'WEBKIT_EXT_texture_filter_anisotropic', 'MOZ_EXT_texture_filter_anisotropic', 
                    'WEBGL_compressed_texture_s3tc', 'WEBGL_depth_texture', 'OES_element_index_uint', 
                    'OES_standard_derivatives', 'OES_vertex_array_object', 'WEBGL_lose_context',
                    'EXT_color_buffer_half_float', 'WEBGL_color_buffer_float', 'WEBGL_compressed_texture_etc'];
    return allowed.includes(name) ? getExt.apply(this, arguments) : null;
}};

WebGLRenderingContext.prototype.getSupportedExtensions = function() {{
    return ['WEBGL_debug_renderer_info', 'EXT_texture_filter_anisotropic', 
            'WEBGL_compressed_texture_s3tc', 'EXT_color_buffer_half_float'];
}};

const origToDataURL = HTMLCanvasElement.prototype.toDataURL;
const origGetImageData = CanvasRenderingContext2D.prototype.getImageData;

function addAdvancedNoise(imageData) {{
    const data = imageData.data;
    const noiseLevel = {random.randint(1, 3)};
    for (let i = 0; i < data.length; i += 4) {{
        if (Math.random() < 0.05) {{
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

const descriptors = {{
    webdriver: {{get: () => undefined}}, platform: {{get: () => '{persona["platform"]}'}},
    hardwareConcurrency: {{get: () => {cores}}}, deviceMemory: {{get: () => {memory}}},
    maxTouchPoints: {{get: () => 0}}, languages: {{get: () => ['{language.split(",")[0]}', 'en']}},
    cookieEnabled: {{get: () => true}}, doNotTrack: {{get: () => null}},
    onLine: {{get: () => true}}, userAgent: {{get: () => '{ua}'}},
    vendor: {{get: () => 'Google Inc.'}}, product: {{get: () => 'Gecko'}},
    productSub: {{get: () => '20030107'}}, vendorSub: {{get: () => ''}}
}};
Object.keys(descriptors).forEach(key => Object.defineProperty(navigator, key, descriptors[key]));

if (navigator.mediaDevices) {{
    const origGetUserMedia = navigator.mediaDevices.getUserMedia;
    navigator.mediaDevices.getUserMedia = function(constraints) {{
        return Promise.reject(new DOMException('Permission denied', 'NotAllowedError'));
    }};
    
    const origEnumerateDevices = navigator.mediaDevices.enumerateDevices;
    navigator.mediaDevices.enumerateDevices = function() {{
        return Promise.resolve([]);
    }};
}}

if (navigator.geolocation) {{
    const origGetCurrentPosition = navigator.geolocation.getCurrentPosition;
    navigator.geolocation.getCurrentPosition = function(success, error, options) {{
        const fakePosition = {{
            coords: {{
                latitude: {location_config["lat"]} + (Math.random() - 0.5) * 0.01,
                longitude: {location_config["lng"]} + (Math.random() - 0.5) * 0.01,
                accuracy: {random.randint(location_config["accuracy"][0], location_config["accuracy"][1])},
                altitude: null, altitudeAccuracy: null, heading: null, speed: null
            }},
            timestamp: Date.now()
        }};
        success(fakePosition);
    }};
}}

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

const automationVars = ['cdc_adoQpoasnfa76pfcZLmcfl_Array', 'cdc_adoQpoasnfa76pfcZLmcfl_Promise', 
                       'cdc_adoQpoasnfa76pfcZLmcfl_Symbol', 'cdc_adoQpoasnfa76pfcZLmcfl_JSON',
                       'cdc_adoQpoasnfa76pfcZLmcfl_Object', 'cdc_adoQpoasnfa76pfcZLmcfl_Proxy'];
automationVars.forEach(v => delete window[v]);

Object.keys(window).forEach(key => {{
    if (key.includes('cdc_') || key.includes('automation') || key.includes('webdriver')) delete window[key];
}});

const screenProps = {{
    width: {{get: () => {width}}}, height: {{get: () => {height}}},
    availWidth: {{get: () => {width}}}, availHeight: {{get: () => {height - random.randint(40, 80)}}},
    colorDepth: {{get: () => 24}}, pixelDepth: {{get: () => 24}},
    orientation: {{get: () => ({{
        angle: 0, type: 'landscape-primary'
    })}}
}};
Object.keys(screenProps).forEach(key => Object.defineProperty(screen, key, screenProps[key]));

const fontMetrics = {{
    'Arial': {{ width: 8.5, height: 12 }},
    'Times New Roman': {{ width: 8.2, height: 11.8 }},
    'Helvetica': {{ width: 8.3, height: 11.9 }},
    'Verdana': {{ width: 8.8, height: 12.2 }}
}};

const origOffsetWidth = Object.getOwnPropertyDescriptor(HTMLElement.prototype, 'offsetWidth');
const origOffsetHeight = Object.getOwnPropertyDescriptor(HTMLElement.prototype, 'offsetHeight');

Object.defineProperty(HTMLElement.prototype, 'offsetWidth', {{
    get: function() {{
        const w = origOffsetWidth.get.apply(this);
        const fontFamily = window.getComputedStyle(this).fontFamily;
        const fontMetric = fontMetrics[fontFamily] || fontMetrics['Arial'];
        return w + (Math.random() < 0.03 ? (Math.random() > 0.5 ? 1 : -1) : 0);
    }}
}});

Object.defineProperty(HTMLElement.prototype, 'offsetHeight', {{
    get: function() {{
        const h = origOffsetHeight.get.apply(this);
        const fontFamily = window.getComputedStyle(this).fontFamily;
        const fontMetric = fontMetrics[fontFamily] || fontMetrics['Arial'];
        return h + (Math.random() < 0.03 ? (Math.random() > 0.5 ? 1 : -1) : 0);
    }}
}});

if (window.performance?.now) {{
    const origNow = window.performance.now;
    const timeOffset = Math.random() * 2000;
    window.performance.now = function() {{ return origNow.apply(this) + timeOffset; }};
}}

if (window.performance?.getEntries) {{
    const origGetEntries = window.performance.getEntries;
    window.performance.getEntries = function() {{
        const entries = origGetEntries.apply(this);
        return entries.map(entry => {{
            entry.duration += (Math.random() - 0.5) * 0.1;
            return entry;
        }});
    }};
}}

if (navigator.getBattery) {{
    const origGetBattery = navigator.getBattery;
    navigator.getBattery = function() {{
        return origGetBattery.apply(this).then(battery => {{
            Object.defineProperties(battery, {{
                level: {{get: () => {battery_level}}}, 
                charging: {{get: () => {str(battery_charging).lower()}}},
                chargingTime: {{get: () => {battery_charging_time}}},
                dischargingTime: {{get: () => {battery_discharging_time}}}
            }});
            return battery;
        }});
    }};
}}

if (navigator.connection) {{
    Object.defineProperties(navigator.connection, {{
        rtt: {{get: () => {connection_rtt}}}, 
        downlink: {{get: () => {connection_downlink}}},
        effectiveType: {{get: () => '{connection_type}'}}, 
        saveData: {{get: () => false}},
        uplink: {{get: () => {connection_uplink}}}
    }});
}}

const origGetTimezoneOffset = Date.prototype.getTimezoneOffset;
Date.prototype.getTimezoneOffset = function() {{ 
    const timezoneOffsets = {{
        'America/New_York': -300, 'Europe/London': 0, 'Europe/Berlin': 60, 'Asia/Tokyo': 540
    }};
    return timezoneOffsets['{timezone}'] || {random.randint(-720, 720)};
}};

if (window.Intl?.DateTimeFormat) {{
    const origResolvedOptions = Intl.DateTimeFormat.prototype.resolvedOptions;
    Intl.DateTimeFormat.prototype.resolvedOptions = function() {{
        const opts = origResolvedOptions.apply(this, arguments);
        opts.timeZone = '{timezone}';
        return opts;
    }};
}}

Object.defineProperties(window, {{
    top: {{get: () => window}}, parent: {{get: () => window}}, frameElement: {{get: () => null}}
}});

if (window.chrome?.runtime) {{
    ['onConnect', 'onMessage', 'sendMessage'].forEach(prop => delete window.chrome.runtime[prop]);
}}

let mouseX = Math.random() * {width}, mouseY = Math.random() * {height};
let lastMouseTime = Date.now();

setInterval(() => {{
    const now = Date.now();
    const timeDiff = now - lastMouseTime;
    
    const speed = Math.random() * 10 + 5;
    const angle = Math.random() * Math.PI * 2;
    
    mouseX += Math.cos(angle) * speed;
    mouseY += Math.sin(angle) * speed;
    mouseX = Math.max(0, Math.min({width}, mouseX));
    mouseY = Math.max(0, Math.min({height}, mouseY));
    
    const event = new MouseEvent('mousemove', {{
        clientX: mouseX, clientY: mouseY, bubbles: true,
        timeStamp: now
    }});
    document.dispatchEvent(event);
    lastMouseTime = now;
}}, Math.random() * 3000 + 1000);

if (navigator.permissions?.query) {{
    const origQuery = navigator.permissions.query;
    navigator.permissions.query = function(obj) {{
        return origQuery.apply(this, arguments).then(result => {{
            if (obj.name === 'notifications') result.state = 'denied';
            if (obj.name === 'geolocation') result.state = 'denied';
            if (obj.name === 'camera') result.state = 'denied';
            if (obj.name === 'microphone') result.state = 'denied';
            return result;
        }});
    }};
}}

Object.defineProperty(navigator, 'hardwareConcurrency', {{
    get: () => {cores}
}});

Object.defineProperty(navigator, 'deviceMemory', {{
    get: () => {memory}
}});

Object.defineProperty(navigator, 'maxTouchPoints', {{
    get: () => 0
}});

delete navigator.__proto__.webdriver;

Object.defineProperty(navigator, 'webdriver', {{
    get: () => undefined
}});

if (window.chrome) {{
    Object.defineProperty(window.chrome, 'runtime', {{
        get: () => undefined
    }});
}}

Object.defineProperty(window, 'selenium', {{
    get: () => undefined
}});

Object.defineProperty(window, 'webdriver', {{
    get: () => undefined
}});

Object.keys(window).forEach(key => {{
    if (key.includes('$cdc') || key.includes('$chrome')) {{
        delete window[key];
    }}
}});
"""

driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': ultimate_stealth_script})

driver.get("https://bot.sannysoft.com/")
time.sleep(random.uniform(4, 8))

for i in range(random.randint(3, 6)):
    scroll_amount = random.randint(150, 400)
    driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
    time.sleep(random.uniform(1.5, 3.5))

driver.execute_script("""
    setTimeout(() => {
        const elements = document.querySelectorAll('div, span, p, button, a');
        const randomEl = elements[Math.floor(Math.random() * elements.length)];
        if (randomEl) {
            randomEl.click();
        }
    }, """ + str(random.randint(2000, 5000)) + """);
""")

driver.execute_script("""
    setTimeout(() => {
        const inputs = document.querySelectorAll('input[type="text"], textarea');
        if (inputs.length > 0) {
            const randomInput = inputs[Math.floor(Math.random() * inputs.length)];
            randomInput.focus();
            randomInput.value = 'test input';
            randomInput.dispatchEvent(new Event('input', { bubbles: true }));
        }
    }, """ + str(random.randint(3000, 6000)) + """);
""")

driver.quit()
shutil.rmtree(profile_dir)