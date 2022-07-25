from selenium import webdriver
from app.application import Application
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


#bs_user = ''
#bs_pw = ''


def browser_init(context):
    """
    :param context: Behave context
    """
    #context.driver = webdriver.Chrome(executable_path='C:\Vallikannu\Learning\chromedriver\chromedriver_07062022.exe')
    context.driver = webdriver.Chrome(executable_path='C:\Vallikannu\Learning\Automation\drivers\chromedriver_win32\chromedriver.exe')

    #FOR FIREFOX -- START
    #opt = Options()
    #opt.binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
    #options.set_preference("browser.download.folderList", 2)
    #options.set_preference("browser.download.manager.showWhenStarting", False)
    #options.set_preference("browser.download.dir", "/Data")
    #options.set_preference("browser.helperApps.neverAsk.saveToDisk",
    #                       "application/octet-stream,application/vnd.ms-excel")
    #context.driver = webdriver.Firefox(
     #   executable_path='C:\Vallikannu\Learning\Automation\drivers\geckodriver_win32\geckodriver.exe', options=opt)

    #FOR FIREFOX -- END

    #context.driver = webdriver.Firefox(executable_path='C:\Vallikannu\Learning\Automation\drivers\geckodriver_win32\geckodriver.exe')
    #context.driver = webdriver.firefox()
    #context.driver = webdriver.Firefox(executable_path='C:\Vallikannu\Learning\Auto_Internship_Gettop_07042022\gettop_internship\geckodriver-v0.31.0-win32\geckodriver.exe')
    #context.driver = webdriver.Firefox(executable_path='C:\Vallikannu\Learning\Auto_Internship_Gettop_07042022\gettop_internship\geckodriver-v0.31.0-win32')
    #context.driver = webdriver.safari()

    # COMMENTED FOLLOWING FOR CHROME
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)


    ### HEADLESS MODE###
    #options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #context.driver = webdriver.Chrome(chrome_options = options)

    # for browserstack #
    #desired_cap = {
    #    'browser: 'Chrome',
    #    'browser_version': '84.0',
    #    'os': 'windows',
    #    'os_version': '10',
    #    'name': name
    #    'browserstack.networkLogs : True
    #}
    #url = f''
    #context.driver = webdriver.Remote(url, desired_capabilities = desired_cap)




def before_scenario(context, scenario):
    # def before_feature(context, scenario)
    # The above line is to run multiple scenario's written in one file, by clicking on feature
    # advantage work faster kill browser automatically and open again for nxt scenario
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    # context.driver.delete_all_cookies()
    context.driver.quit()
