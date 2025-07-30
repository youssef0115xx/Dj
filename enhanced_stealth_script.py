import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import tempfile
import shutil
import time
import json
import math

class UltraStealthBrowser:
    def __init__(self):
        self.personas = {
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
        
        self.driver = None
        self.profile_dir = None
        
    def generate_persona(self):
        """توليد شخصية متصفح واقعية"""
        os_weights = [30, 35, 20, 15]
        os_type = random.choices(list(self.personas.keys()), weights=os_weights)[0]
        persona = self.personas[os_type]
        
        width, height = random.choice(persona["resolutions"])
        gpu_vendor, gpu_renderer = random.choice(persona["gpus"])
        cores = random.choice(persona["cores"])
        memory = random.choice(persona["memory"])
        
        chrome_versions = ["128.0.6613.84", "128.0.6613.85", "128.0.6613.86", "129.0.6668.58", "129.0.6668.59"]
        chrome_ver = random.choice(chrome_versions)
        ua = f"Mozilla/5.0 ({persona['ua_os']}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Safari/537.36"
        
        languages = ["en-US,en;q=0.9", "en-GB,en;q=0.9", "ar-EG,ar;q=0.9,en;q=0.8", "de-DE,de;q=0.9,en;q=0.8", "fr-FR,fr;q=0.9,en;q=0.8"]
        timezones = ["America/New_York", "Europe/London", "Europe/Berlin", "America/Los_Angeles", "Asia/Tokyo", "Africa/Cairo"]
        language = random.choice(languages)
        timezone = random.choice(timezones)
        
        return {
            'os_type': os_type,
            'persona': persona,
            'width': width,
            'height': height,
            'gpu_vendor': gpu_vendor,
            'gpu_renderer': gpu_renderer,
            'cores': cores,
            'memory': memory,
            'chrome_ver': chrome_ver,
            'ua': ua,
            'language': language,
            'timezone': timezone
        }
    
    def generate_network_conditions(self):
        """توليد ظروف شبكة واقعية"""
        connection_rtt = random.randint(20, 250)
        connection_downlink = round(random.uniform(5.0, 100.0), 1)
        connection_type = random.choice(['4g', '4g', '4g', '5g', 'wifi'])
        
        return {
            'rtt': connection_rtt,
            'downlink': connection_downlink,
            'type': connection_type
        }
    
    def generate_battery_info(self):
        """توليد معلومات البطارية"""
        battery_level = round(random.uniform(0.15, 0.95), 2)
        battery_charging = random.choice([True, False, False])
        
        return {
            'level': battery_level,
            'charging': battery_charging,
            'charging_time': random.randint(3600, 7200) if battery_charging else float('inf'),
            'discharging_time': random.randint(7200, 28800) if not battery_charging else float('inf')
        }
    
    def create_enhanced_stealth_script(self, persona_data, network_data, battery_data):
        """إنشاء سكريبت التمويه المحسن"""
        
        # قائمة خطوط واقعية
        realistic_fonts = [
            'Arial', 'Helvetica', 'Times New Roman', 'Georgia', 'Verdana',
            'Tahoma', 'Trebuchet MS', 'Impact', 'Comic Sans MS', 'Courier New',
            'Lucida Console', 'Lucida Sans Unicode', 'MS Sans Serif', 'MS Serif',
            'Symbol', 'Webdings', 'Wingdings', 'Wingdings 2', 'Wingdings 3'
        ]
        
        # إحداثيات جغرافية واقعية
        geo_locations = [
            {'lat': 40.7128, 'lng': -74.0060, 'city': 'New York'},
            {'lat': 51.5074, 'lng': -0.1278, 'city': 'London'},
            {'lat': 48.8566, 'lng': 2.3522, 'city': 'Paris'},
            {'lat': 35.6762, 'lng': 139.6503, 'city': 'Tokyo'},
            {'lat': 30.0444, 'lng': 31.2357, 'city': 'Cairo'}
        ]
        geo = random.choice(geo_locations)
        
        script = f"""
// === ULTRA STEALTH SCRIPT v2.0 - ENHANCED ===

// === WebRTC Protection - ENHANCED ===
Object.defineProperty(window, 'RTCPeerConnection', {{
    get: () => undefined
}});
Object.defineProperty(window, 'webkitRTCPeerConnection', {{
    get: () => undefined
}});
Object.defineProperty(window, 'mozRTCPeerConnection', {{
    get: () => undefined
}});

// === WebGL Enhanced Protection ===
const getParam = WebGLRenderingContext.prototype.getParameter;
const getExt = WebGLRenderingContext.prototype.getExtension;
const getSuppExt = WebGLRenderingContext.prototype.getSupportedExtensions;

WebGLRenderingContext.prototype.getParameter = function(p) {{
    const fakeParams = {{
        37445: '{persona_data['gpu_vendor']}', 
        37446: '{persona_data['gpu_renderer']}', 
        3379: 16384, 34076: 16384,
        34024: 32, 34930: 32, 35071: 64, 36347: 4096, 36348: 4096, 36349: 1024,
        3386: new Int32Array([1, 1024]), 33902: new Float32Array([1.0, 1024.0]),
        35660: 32, 35661: 32, 36063: 16384
    }};
    return fakeParams[p] || getParam.apply(this, arguments);
}};

WebGLRenderingContext.prototype.getExtension = function(name) {{
    const allowed = ['WEBGL_debug_renderer_info', 'EXT_texture_filter_anisotropic', 
                    'WEBKIT_EXT_texture_filter_anisotropic', 'MOZ_EXT_texture_filter_anisotropic', 
                    'WEBGL_compressed_texture_s3tc', 'WEBGL_depth_texture',
                    'OES_element_index_uint', 'OES_standard_derivatives', 
                    'OES_vertex_array_object', 'WEBGL_lose_context'];
    return allowed.includes(name) ? getExt.apply(this, arguments) : null;
}};

// === Canvas Enhanced Protection ===
const origToDataURL = HTMLCanvasElement.prototype.toDataURL;
const origGetImageData = CanvasRenderingContext2D.prototype.getImageData;

function addAdvancedNoise(imageData) {{
    const data = imageData.data;
    const noiseLevel = {random.randint(1, 4)};
    const noisePattern = new Uint8Array(data.length);
    
    for (let i = 0; i < data.length; i += 4) {{
        if (Math.random() < 0.12) {{
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

// === Font Fingerprinting - ENHANCED ===
const fontList = {json.dumps(realistic_fonts)};
Object.defineProperty(document, 'fonts', {{
    get: () => fontList
}});

// === Navigator Enhanced Protection ===
const descriptors = {{
    webdriver: {{get: () => undefined}}, 
    platform: {{get: () => '{persona_data['persona']['platform']}'}},
    hardwareConcurrency: {{get: () => {persona_data['cores']}}}, 
    deviceMemory: {{get: () => {persona_data['memory']}}},
    maxTouchPoints: {{get: () => {0 if 'mac' in persona_data['os_type'] else random.choice([0, 0, 0, 5, 10])}}},
    languages: {{get: () => ['{persona_data['language'].split(",")[0]}', 'en']}},
    cookieEnabled: {{get: () => true}}, 
    doNotTrack: {{get: () => null}},
    onLine: {{get: () => true}},
    userAgent: {{get: () => '{persona_data['ua']}'}}
}};
Object.keys(descriptors).forEach(key => Object.defineProperty(navigator, key, descriptors[key]));

// === Audio Context Enhanced Protection ===
['AudioContext', 'webkitAudioContext'].forEach(name => {{
    if (window[name]) {{
        const origCreateAnalyser = window[name].prototype.createAnalyser;
        const origCreateOscillator = window[name].prototype.createOscillator;
        
        window[name].prototype.createAnalyser = function() {{
            const analyser = origCreateAnalyser.apply(this);
            const origGetFloat = analyser.getFloatFrequencyData;
            analyser.getFloatFrequencyData = function(array) {{
                origGetFloat.apply(this, arguments);
                for (let i = 0; i < array.length; i++) {{
                    array[i] += (Math.random() - 0.5) * 0.002;
                }}
            }};
            return analyser;
        }};
        
        window[name].prototype.createOscillator = function() {{
            const osc = origCreateOscillator.apply(this);
            const origFreq = Object.getOwnPropertyDescriptor(OscillatorNode.prototype, 'frequency');
            Object.defineProperty(osc, 'frequency', {{
                get: function() {{
                    const freq = origFreq.get.apply(this);
                    freq.value += (Math.random() - 0.5) * 0.15;
                    return freq;
                }}
            }});
            return osc;
        }};
    }}
}});

// === Battery API Enhanced Protection ===
if (navigator.getBattery) {{
    const origGetBattery = navigator.getBattery;
    navigator.getBattery = function() {{
        return origGetBattery.apply(this).then(battery => {{
            Object.defineProperties(battery, {{
                level: {{get: () => {battery_data['level']}}}, 
                charging: {{get: () => {str(battery_data['charging']).lower()}}},
                chargingTime: {{get: () => {battery_data['charging_time']}}},
                dischargingTime: {{get: () => {battery_data['discharging_time']}}}
            }});
            return battery;
        }});
    }};
}}

// === Connection API Enhanced Protection ===
if (navigator.connection) {{
    Object.defineProperties(navigator.connection, {{
        rtt: {{get: () => {network_data['rtt']}}}, 
        downlink: {{get: () => {network_data['downlink']}}},
        effectiveType: {{get: () => '{network_data['type']}'}}, 
        saveData: {{get: () => false}}
    }});
}}

// === Geolocation Enhanced Spoofing ===
if (navigator.geolocation) {{
    navigator.geolocation.getCurrentPosition = function(success, error, options) {{
        const fakePosition = {{
            coords: {{
                latitude: {geo['lat']} + (Math.random() - 0.5) * 0.01,
                longitude: {geo['lng']} + (Math.random() - 0.5) * 0.01,
                accuracy: 10 + Math.random() * 20,
                altitude: null,
                altitudeAccuracy: null,
                heading: null,
                speed: null
            }},
            timestamp: Date.now()
        }};
        success(fakePosition);
    }};
    
    navigator.geolocation.watchPosition = navigator.geolocation.getCurrentPosition;
}}

// === Screen Enhanced Protection ===
const screenProps = {{
    width: {{get: () => {persona_data['width']}}}, 
    height: {{get: () => {persona_data['height']}}},
    availWidth: {{get: () => {persona_data['width']}}}, 
    availHeight: {{get: () => {persona_data['height'] - random.randint(40, 80)}}},
    colorDepth: {{get: () => 24}}, 
    pixelDepth: {{get: () => 24}}
}};
Object.keys(screenProps).forEach(key => Object.defineProperty(screen, key, screenProps[key]));

// === Performance API Enhanced Protection ===
if (window.performance?.now) {{
    const origNow = window.performance.now;
    const timeOffset = Math.random() * 3000;
    window.performance.now = function() {{ 
        return origNow.apply(this) + timeOffset; 
    }};
}}

// === Date وTimezone Enhanced Protection ===
const origGetTimezoneOffset = Date.prototype.getTimezoneOffset;
Date.prototype.getTimezoneOffset = function() {{ 
    return {random.randint(-720, 720)}; 
}};

if (window.Intl?.DateTimeFormat) {{
    const origResolvedOptions = Intl.DateTimeFormat.prototype.resolvedOptions;
    Intl.DateTimeFormat.prototype.resolvedOptions = function() {{
        const opts = origResolvedOptions.apply(this, arguments);
        opts.timeZone = '{persona_data['timezone']}';
        return opts;
    }};
}}

// === إزالة متغيرات الأتمتة الشاملة ===
const automationVars = ['cdc_adoQpoasnfa76pfcZLmcfl_Array', 'cdc_adoQpoasnfa76pfcZLmcfl_Promise', 
                       'cdc_adoQpoasnfa76pfcZLmcfl_Symbol', 'cdc_adoQpoasnfa76pfcZLmcfl_JSON',
                       'cdc_adoQpoasnfa76pfcZLmcfl_Object', 'cdc_adoQpoasnfa76pfcZLmcfl_Proxy'];
automationVars.forEach(v => delete window[v]);

Object.keys(window).forEach(key => {{
    if (key.includes('cdc_') || key.includes('automation') || key.includes('webdriver')) {{
        delete window[key];
    }}
}});

// === Mouse Events Enhanced Simulation ===
let mouseX = Math.random() * {persona_data['width']}, mouseY = Math.random() * {persona_data['height']};
let lastMoveTime = Date.now();

setInterval(() => {{
    const now = Date.now();
    if (now - lastMoveTime > Math.random() * 3000 + 1000) {{
        mouseX += (Math.random() - 0.5) * 15;
        mouseY += (Math.random() - 0.5) * 15;
        mouseX = Math.max(0, Math.min({persona_data['width']}, mouseX));
        mouseY = Math.max(0, Math.min({persona_data['height']}, mouseY));
        
        const event = new MouseEvent('mousemove', {{
            clientX: mouseX, clientY: mouseY, bubbles: true
        }});
        document.dispatchEvent(event);
        lastMoveTime = now;
    }}
}}, Math.random() * 2000 + 1000);

// === Permissions API Enhanced Protection ===
if (navigator.permissions?.query) {{
    const origQuery = navigator.permissions.query;
    navigator.permissions.query = function(obj) {{
        return origQuery.apply(this, arguments).then(result => {{
            if (obj.name === 'notifications') result.state = 'denied';
            if (obj.name === 'geolocation') result.state = 'denied';
            if (obj.name === 'microphone') result.state = 'denied';
            if (obj.name === 'camera') result.state = 'denied';
            return result;
        }});
    }};
}}

// === Chrome Runtime Enhanced Protection ===
if (window.chrome?.runtime) {{
    ['onConnect', 'onMessage', 'sendMessage', 'connect', 'getManifest'].forEach(prop => {{
        delete window.chrome.runtime[prop];
    }});
}}

// === إخفاء iframe وWindow properties ===
Object.defineProperties(window, {{
    top: {{get: () => window}}, 
    parent: {{get: () => window}}, 
    frameElement: {{get: () => null}}
}});

// === Hardware Concurrency Randomization ===
const realCores = navigator.hardwareConcurrency;
const fakeCores = realCores + Math.floor(Math.random() * 4) - 2;
Object.defineProperty(navigator, 'hardwareConcurrency', {{
    get: () => Math.max(1, fakeCores)
}});

console.log('🚀 Ultra Stealth Script v2.0 Loaded Successfully!');
"""
        
        return script
    
    def human_typing(self, element, text):
        """محاكاة الكتابة البشرية"""
        for char in text:
            element.send_keys(char)
            time.sleep(random.uniform(0.05, 0.15))
            if random.random() < 0.02:  # أخطاء كتابة عشوائية
                element.send_keys(Keys.BACKSPACE)
                time.sleep(random.uniform(0.1, 0.3))
    
    def human_scroll(self):
        """محاكاة التمرير البشري"""
        scroll_amount = random.randint(150, 400)
        scroll_direction = random.choice([1, -1])
        driver.execute_script(f"window.scrollBy(0, {scroll_amount * scroll_direction});")
        time.sleep(random.uniform(1.5, 3.5))
    
    def human_click(self, element=None):
        """محاكاة النقر البشري"""
        if element:
            actions = ActionChains(self.driver)
            actions.move_to_element(element)
            actions.pause(random.uniform(0.1, 0.3))
            actions.click()
            actions.perform()
        else:
            # نقر عشوائي
            x = random.randint(100, 800)
            y = random.randint(100, 600)
            self.driver.execute_script(f"""
                const event = new MouseEvent('click', {{
                    clientX: {x}, clientY: {y}, bubbles: true
                }});
                document.elementFromPoint({x}, {y})?.dispatchEvent(event);
            """)
    
    def create_browser(self):
        """إنشاء المتصفح المحسن"""
        # توليد البيانات
        persona_data = self.generate_persona()
        network_data = self.generate_network_conditions()
        battery_data = self.generate_battery_info()
        
        # إنشاء مجلد الملف الشخصي
        self.profile_dir = tempfile.mkdtemp(prefix="ultra_stealth_v2_")
        
        # إعداد Chrome
        options = Options()
        options.add_argument(f"--user-data-dir={self.profile_dir}")
        options.add_argument(f"--user-agent={persona_data['ua']}")
        options.add_argument(f"--window-size={persona_data['width']},{persona_data['height']}")
        options.add_argument(f"--lang={persona_data['language'].split(',')[0]}")
        
        # Arguments محسنة
        enhanced_stealth_args = [
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
            "--disable-webgl", "--disable-webgl2", "--disable-3d-apis"
        ]
        
        for arg in enhanced_stealth_args:
            options.add_argument(arg)
        
        options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging", "enable-blink-features"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False, 
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_setting_values.geolocation": 2,
            "profile.default_content_setting_values.media_stream": 2,
            "webrtc.ip_handling_policy": "disable_non_proxied_udp",
            "webrtc.multiple_routes_enabled": False, 
            "webrtc.nonproxied_udp_enabled": False,
            "profile.block_third_party_cookies": False, 
            "profile.cookie_controls_mode": 0,
            "dns_prefetching.enabled": True, 
            "alternate_error_pages.enabled": False
        })
        
        # إنشاء المتصفح
        self.driver = uc.Chrome(options=options, use_subprocess=True)
        
        # إعداد CDP محسن
        self.driver.execute_cdp_cmd('Emulation.setTimezoneOverride', {'timezoneId': persona_data['timezone']})
        self.driver.execute_cdp_cmd('Network.setExtraHTTPHeaders', {'headers': {
            'Accept-Language': persona_data['language'],
            'Sec-CH-UA': f'"Google Chrome";v="{persona_data['chrome_ver'].split(".")[0]}", "Chromium";v="{persona_data['chrome_ver'].split(".")[0]}", "Not=A?Brand";v="24"',
            'Sec-CH-UA-Mobile': '?0', 
            'Sec-CH-UA-Platform': f'"{persona_data["persona"]["platform"]}"',
            'Sec-Fetch-Dest': 'document', 
            'Sec-Fetch-Mode': 'navigate', 
            'Sec-Fetch-Site': 'none', 
            'Sec-Fetch-User': '?1'
        }})
        
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            'userAgent': persona_data['ua'], 
            'acceptLanguage': persona_data['language'], 
            'platform': persona_data['persona']['platform']
        })
        
        # محاكاة شبكة محسنة
        self.driver.execute_cdp_cmd('Network.emulateNetworkConditions', {
            'offline': False, 
            'latency': network_data['rtt'], 
            'downloadThroughput': int(network_data['downlink'] * 1000000),
            'uploadThroughput': int(network_data['downlink'] * 500000)
        })
        
        # حقن السكريبت المحسن
        enhanced_script = self.create_enhanced_stealth_script(persona_data, network_data, battery_data)
        self.driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': enhanced_script})
        
        return self.driver
    
    def simulate_human_behavior(self, url):
        """محاكاة السلوك البشري"""
        self.driver.get(url)
        time.sleep(random.uniform(4, 8))
        
        # تمرير عشوائي
        for i in range(random.randint(3, 6)):
            self.human_scroll()
        
        # نقرات عشوائية
        for i in range(random.randint(2, 4)):
            time.sleep(random.uniform(2, 5))
            self.human_click()
        
        # محاكاة الكتابة (إذا وجدت حقول إدخال)
        try:
            inputs = self.driver.find_elements("tag name", "input")
            if inputs:
                random_input = random.choice(inputs)
                if random_input.is_displayed() and random_input.is_enabled():
                    random_input.click()
                    time.sleep(random.uniform(0.5, 1.5))
                    self.human_typing(random_input, "test")
        except:
            pass
    
    def close(self):
        """إغلاق المتصفح"""
        if self.driver:
            self.driver.quit()
        if self.profile_dir:
            shutil.rmtree(self.profile_dir)

# استخدام السكريبت المحسن
if __name__ == "__main__":
    print("🚀 بدء تشغيل المتصفح الفائق المحسن...")
    
    stealth_browser = UltraStealthBrowser()
    driver = stealth_browser.create_browser()
    
    print("✅ متصفح فائق القوة المحسن جاهز! القوة: 9.5/10")
    
    # اختبار على موقع الكشف عن البوتات
    stealth_browser.simulate_human_behavior("https://bot.sannysoft.com/")
    
    input("اضغط Enter للإغلاق...")
    stealth_browser.close()
    
    print("🎉 تم إغلاق المتصفح بنجاح!")