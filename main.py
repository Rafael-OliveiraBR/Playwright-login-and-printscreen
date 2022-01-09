###########################################################
"""
    esse é um simples script para automatizar o login
    de um site, acessar uma página e fazer um print
    da tela do navegador, de forma automatizada.
    o mesmo exemplo pode ser usado para testes ou
    coletar informações de sites/páginas.

    AUTOR: Rafael Santos de Oliveira
    github: https://github.com/Rafael-OliveiraBR
    linkedin: https://www.linkedin.com/in/rafael-oliveira-16366389/

"""
###########################################################

# imports
from playwright.sync_api import sync_playwright
from account import *


###########################################################
#   SETUP DO BROWSER, EXECUÇÃO DAS AUTOMAÇÕES
###########################################################
with sync_playwright() as p:
    """ Executa com o browser aberto, faz um vídeo da execução"""
    browser = p.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context(
        record_video_dir="videos/",
        record_video_size={"width": 640, "height": 480}
    )
    page = context.new_page()
    page.goto('https://github.com')


    # --------------------------
    # EXECUTA AÇÕES
    # --------------------------
    """ Faz login, acessa perfil, tira print e desloga da conta """
    page.click("text=Sign in")
    page.fill('input[name="login"]', user)
    page.fill('input[name="password"]', password)
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

    # Salva dados armazenados em um arquivo
    storage = context.storage_state(path="state.json")

    # Cria um novo context com os dados salvos.
    context = browser.new_context(storage_state="state.json")

    # fecha browser
    context.close()
