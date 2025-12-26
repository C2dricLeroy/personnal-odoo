def install_fr(env):
    lang = env['res.lang'].with_context(active_test=False).search([('code', '=', "fr_FR")], limit=1)
    if lang:
        wizard = env["base.language.install"].create({
            'lang_ids': [(4, 0, lang.ids)],
        })
        wizard.lang_install()


def post_init_hook(env):   
    install_fr(env)