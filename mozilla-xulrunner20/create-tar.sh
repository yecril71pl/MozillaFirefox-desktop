#!/bin/bash

BRANCH="mozilla-central"
RELEASE_TAG="FIREFOX_4_0b12_RELEASE"
VERSION="2.0b12"

# mozilla
hg clone http://hg.mozilla.org/$BRANCH mozilla
pushd mozilla
[ "$RELEASE_TAG" == "default" ] || hg update -r $RELEASE_TAG
popd
tar cjf xulrunner-source-$VERSION.tar.bz2 --exclude=.hgtags --exclude=.hgignore --exclude=.hg --exclude=CVS mozilla

# l10n
test ! -d l10n && mkdir l10n
for locale in $(awk '{ print $1; }' mozilla/browser/locales/shipped-locales); do
  case $locale in
    ja-JP-mac|en-US)
      ;;
    *)
      hg clone http://hg.mozilla.org/l10n-central/$locale l10n/$locale
      [ "$RELEASE_TAG" == "default" ] || hg -R l10n/$locale up -C -r $RELEASE_TAG
      ;;
  esac
done
tar cjf l10n-$VERSION.tar.bz2 --exclude=.hgtags --exclude=.hgignore --exclude=.hg l10n

# compare-locales
hg clone http://hg.mozilla.org/build/compare-locales
tar cjf compare-locales.tar.bz2 --exclude=.hgtags --exclude=.hgignore --exclude=.hg compare-locales

