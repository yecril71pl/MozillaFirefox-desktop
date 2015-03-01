#!/bin/bash

CHANNEL="beta"
BRANCH="releases/mozilla-$CHANNEL"
RELEASE_TAG="FIREFOX_37_0b1_RELEASE"
VERSION="36.99"

# mozilla
if [ -d mozilla ]; then
  pushd mozilla
  _repourl=$(hg paths)
  case "$_repourl" in
    *$BRANCH*)
      echo "updating previous tree"
      hg pull
      popd
      ;;
    * )
      echo "removing obsolete tree"
      popd
      rm -rf mozilla
      ;;
  esac
fi
if [ ! -d mozilla ]; then
  echo "cloning new $BRANCH..."
  hg clone http://hg.mozilla.org/$BRANCH mozilla
fi
pushd mozilla
hg update --check
[ "$RELEASE_TAG" == "default" ] || hg update -r $RELEASE_TAG
# get repo and source stamp
echo -n "REV=" > ../source-stamp.txt
hg -R . parent --template="{node|short}\n" >> ../source-stamp.txt
echo -n "REPO=" >> ../source-stamp.txt
hg showconfig paths.default 2>/dev/null | head -n1 | sed -e "s/^ssh:/http:/" >> ../source-stamp.txt
popd
echo "creating archive..."
tar cJf firefox-$VERSION-source.tar.xz --exclude=.hgtags --exclude=.hgignore --exclude=.hg --exclude=CVS mozilla

# l10n
echo "fetching locales..."
test ! -d l10n && mkdir l10n
for locale in $(awk '{ print $1; }' mozilla/browser/locales/shipped-locales); do
  case $locale in
    ja-JP-mac|en-US)
      ;;
    *)
      echo "fetching $locale ..."
      hg clone http://hg.mozilla.org/releases/l10n/mozilla-$CHANNEL/$locale l10n/$locale
      [ "$RELEASE_TAG" == "default" ] || hg -R l10n/$locale up -C -r $RELEASE_TAG
      ;;
  esac
done
echo "creating l10n archive..."
tar cJf l10n-$VERSION.tar.xz --exclude=.hgtags --exclude=.hgignore --exclude=.hg l10n

# compare-locales
echo "creating compare-locales"
hg clone http://hg.mozilla.org/build/compare-locales
tar cJf compare-locales.tar.xz --exclude=.hgtags --exclude=.hgignore --exclude=.hg compare-locales

