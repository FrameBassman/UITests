from selenium.webdriver.common.by import By

class RegistrationPageLocators(object):

    SUBMIT = (By.ID, 'submitbutton')

class InboxPageLocators(object):

    SEND_BUTTON = (By.ID, ':o4')

class LoginPageLocators(object):

    NEXT = (By.ID, 'next')
    SIGNIN = (By.ID, 'signIn')

class LogoutLocators(object):
    FLYOUTMENU = (By.CSS_SELECTOR, 'html.aAX body.aAU div div.nH div.nH div.nH.w-asV.aiw div.nH.oy8Mbf.qp div#gb.gb_6e.gb_T div.gb_ge.gb_9e div.gb_bb.gb_9e.gb_R.gb_8e.gb_T div.gb_cc.gb_9e.gb_R div.gb_8a.gb_wc.gb_9e.gb_R div.gb_nc.gb_ab.gb_9e.gb_R a.gb_b.gb_6a.gb_R span.gb_1a.gbii')
    SIGNOUT = (By.CSS_SELECTOR, 'html.aAX body.aAU div div.nH div.nH div.nH.w-asV.aiw div.nH.oy8Mbf.qp div#gb.gb_6e.gb_T div.gb_ge.gb_9e div.gb_bb.gb_9e.gb_R.gb_8e.gb_T div.gb_cc.gb_9e.gb_R div.gb_8a.gb_wc.gb_9e.gb_R.gb_g div.gb_eb.gb_ga.gb_g div.gb_qb div a#gb_71.gb_Da.gb_le.gb_se.gb_pb')
    ACCOUNTCHOOSER = (By.ID , 'account-chooser-link')
    ADDACCOUNT = (By.ID, 'account-chooser-add-account')

class EmailLocators(object):
    SUBJ = (By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div[1]/div[1]/div/div/div[7]/div/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[6]/div/div/div/span[1]")
    BODY = (By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div[1]/div[1]/div/div/div[7]/div/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[6]/div/div/div/span[2]")

class ConfirmationMessage(object):
    Message = (By.CSS_SELECTOR, "#link_vsm")