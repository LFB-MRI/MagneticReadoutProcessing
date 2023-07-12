def save(self, page: Page, text, summary=u'', minor=False, bot=True, section=None, **kwargs):
    """
    Performs a page edit, retrying the login once if the edit fails due to the user being logged out

    This function hopefully makes it easy to workaround the lag and frequent login timeouts
    experienced on the Fandom UCP platform compared to Gamepedia Hydra.

    :param page: mwclient Page object
    :param text: as in mwclient.Page.edit
    :param summary: as in mwclient.Page.edit
    :param minor: as in mwclient.Page.edit
    :param bot: as in mwclient.Page.edit
    :param section: as in mwclient.Page.edit
    :param kwargs: as in mwclient.Page.edit
    :return: nothing