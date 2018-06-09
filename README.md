# OpenStack Client Config #

This project will:

- create a sample set of configurations in `~/.config/openstack`
- create a python virtualenv in [pyenv/](pyenv/) compatible with Newton

# Instructions #

- Run [setup-env](setup-env) which assumes you have python3 and it's devel libs (such as python34-devel) installed.
- Activate virtualenv: `. pyenv/bin/activate`.
- Run [client-config.yaml](client-config.yaml) Ansible playbook to set up your `~/.config/openstack` directory.
- Source the autocompletion hints dropped by the playbook `. ~/.bash_completion.d/osc`
- Use [unset.sh](unset.sh) to ensure you are using openstack client config and not env vars. You may wish to set `OS_CLOUD` though.
- Try `openstack --os-cloud $USER flavor list`.

# Links #

- https://docs.openstack.org/ocata/user-guide/cli.html
- https://docs.openstack.org/ocata/user-guide/cli-cheat-sheet.html
- https://docs.openstack.org/os-client-config/latest/user/index.html
- https://docs.openstack.org/python-openstackclient/latest/configuration/index.html
- https://docs.openstack.org/ocata/user-guide/common/cli-install-openstack-command-line-clients.html
