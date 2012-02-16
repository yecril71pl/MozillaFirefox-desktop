#!/bin/bash

RELEASE_TAG="FIREFOX_3_6_27_RELEASE"
VERSION="1.9.2.27"

# mozilla
hg clone http://hg.mozilla.org/releases/mozilla-1.9.2 mozilla
pushd mozilla
hg update -r $RELEASE_TAG
popd
tar cjf xulrunner-source-$VERSION.tar.bz2 --exclude=.hgtags --exclude=.hgignore --exclude=.hg --exclude=CVS mozilla

# l10n
test ! -d l10n && mkdir l10n
for locale in $(awk '{ print $1; }' mozilla/browser/locales/shipped-locales); do
  case $locale in
    ja-JP-mac|en-US)
      ;;
    *)
      hg clone http://hg.mozilla.org/releases/l10n-mozilla-1.9.2/$locale l10n/$locale
      hg -R l10n/$locale up -C -r $RELEASE_TAG
      ;;
  esac
done
tar cjf l10n-$VERSION.tar.bz2 --exclude=.hgtags --exclude=.hgignore --exclude=.hg l10n

