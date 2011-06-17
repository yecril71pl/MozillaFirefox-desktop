#!/bin/bash

BRANCH="mozilla-beta"
RELEASE_TAG="FIREFOX_5_0b7_RELEASE"
VERSION="4.99"

# mozilla
hg clone http://hg.mozilla.org/$BRANCH mozilla
pushd mozilla
[ "$RELEASE_TAG" == "default" ] || hg update -r $RELEASE_TAG
# get repo and source stamp
echo -n "REV=" > ../source-stamp.txt
hg -R . parent --template="{node|short}\n" >> ../source-stamp.txt
echo -n "REPO=" >> ../source-stamp.txt
hg showconfig paths.default 2>/dev/null | head -n1 | sed -e "s/^ssh:/http:/" >> ../source-stamp.txt
popd
tar cjf firefox-$VERSION-source.tar.bz2 --exclude=.hgtags --exclude=.hgignore --exclude=.hg --exclude=CVS mozilla

# l10n
test ! -d l10n && mkdir l10n
for locale in $(awk '{ print $1; }' mozilla/browser/locales/shipped-locales); do
  case $locale in
    ja-JP-mac|en-US)
      ;;
    *)
      hg clone http://hg.mozilla.org/releases/l10n/mozilla-beta/$locale l10n/$locale
      [ "$RELEASE_TAG" == "default" ] || hg -R l10n/$locale up -C -r $RELEASE_TAG
      ;;
  esac
done
tar cjf l10n-$VERSION.tar.bz2 --exclude=.hgtags --exclude=.hgignore --exclude=.hg l10n

# compare-locales
hg clone http://hg.mozilla.org/build/compare-locales
tar cjf compare-locales.tar.bz2 --exclude=.hgtags --exclude=.hgignore --exclude=.hg compare-locales

