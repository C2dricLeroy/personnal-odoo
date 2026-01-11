def install_fr(env):
    lang = env['res.lang'].with_context(active_test=False).search([('code', '=', "fr_FR")], limit=1)
    if lang and not lang.active:
        try:
            wizard = env["base.language.install"].create({
                'lang_ids': [(4, lang.ids)],
            })
            wizard.lang_install()
        except Exception as e:
            print(f'Error installing French language: {e}')


def post_init_hook(env):   
    install_fr(env)