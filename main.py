from playwright.sync_api import sync_playwright


###########################################################
#   SETUP BROWSER
###########################################################
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://github.com')


    # --------------------------
    # EXECUTE ACTIONS
    # --------------------------
    """ Faz login, acessa perfil, tira print e desloga da conta """
    page.click("text=Sign in")
    page.fill('input[name="login"]', 'rsdo@outlook.com')
    page.fill('input[name="password"]', 'redbanger33')
    page.click('input[name="commit"]')
    #page.wait_for_timeout(1000)
    page.click('[aria-label="View profile and more"]')
    #page.wait_for_timeout(1000)
    page.click('[data-ga-click="Header, go to profile, text:your profile"]')
    page.wait_for_timeout(2000)
    page.screenshot(path="github profile.png")
    page.screenshot(path="github profile full.png", full_page=True)
    #page.wait_for_timeout(1000)
    page.click('[aria-label="View profile and more"]')
    #page.wait_for_timeout(2000)
    page.click('[class="dropdown-item dropdown-signout"]')
    #page.wait_for_timeout(4000)

    # Save storage state into the file.
    storage = context.storage_state(path="state.json")

    # Create a new context with the saved storage state.
    context = browser.new_context(storage_state="state.json")

