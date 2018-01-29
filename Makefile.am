pkgprefdir = $(pkglibdir)/defaults/preferences
pkgbrowprefdir = $(pkglibdir)/browser/defaults/preferences
appdir = $(datadir)/applications
mimepackdir = $(datadir)/mime/packages

pkgpref_DATA = MozillaFirefox/spellcheck.js
pkgbrowpref_DATA = MozillaFirefox/kde.js MozillaFirefox/firefox.js
pkglibexec_SCRIPTS = MozillaFirefox/firefox.sh
bin_PROGRAMS = firefox
app_DATA = MozillaFirefox/MozillaFirefox.desktop
mimepack_DATA = MozillaFirefox/firefox.xml

firefox$(EXEEXT):
	ln '-sT' '$(pkglibexecdir)/firefox.sh' '$(@)'
