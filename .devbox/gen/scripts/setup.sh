set -e

if [ -z "$__DEVBOX_SKIP_INIT_HOOK_418f11e2a55bddb499af65476bd937438bf9896058b568a91bc9263f5c0df3bf" ]; then
    . "/Volumes/SSD2TB/work/antigravity/py_kvdt/.devbox/gen/scripts/.hooks.sh"
fi

uv pip install -e .
