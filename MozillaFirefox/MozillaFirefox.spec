#
# spec file for package MozillaFirefox
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#               2006-2012 Wolfgang Rosenauer
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define major 9
%define mainver %major.99

Name:           MozillaFirefox
BuildRequires:  Mesa-devel
BuildRequires:  autoconf213
BuildRequires:  dbus-1-glib-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  libgnomeui-devel
BuildRequires:  libidl-devel
BuildRequires:  libnotify-devel
BuildRequires:  python
BuildRequires:  startup-notification-devel
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  yasm
BuildRequires:  zip
%if %suse_version > 1110
BuildRequires:  libiw-devel
BuildRequires:  libproxy-devel
%else
BuildRequires:  wireless-tools
%endif
BuildRequires:  mozilla-nspr-devel >= 4.8.9
BuildRequires:  mozilla-nss-devel >= 3.13.1
BuildRequires:  nss-shared-helper-devel
Version:        %{mainver}
Release:        10
%define         releasedate 2012011800
Provides:       web_browser
Provides:       firefox = %{version}-%{release}
Provides:       firefox = %{mainver}
# this is needed to match this package with the kde4 helper package without the main package
# having a hard requirement on the kde4 package
%define kde_helper_version 6
Provides:       mozilla-kde4-version = %{kde_helper_version}
Summary:        Mozilla Firefox Web Browser
License:        MPL-1.1 or GPL-2.0+ or LGPL-2.1+
Group:          Productivity/Networking/Web/Browsers
Url:            http://www.mozilla.org/
Source:         firefox-%{version}-source.tar.bz2
Source1:        MozillaFirefox.desktop
Source2:        MozillaFirefox-rpmlintrc
Source3:        mozilla.sh.in
Source4:        find-external-requires.sh
Source5:        source-stamp.txt
Source6:        kde.js
Source7:        l10n-%{version}.tar.bz2
Source8:        firefox-mimeinfo.xml
Source10:       compare-locales.tar.bz2
Source11:       firefox.1
Source12:       mozilla-get-app-id
Source13:       add-plugins.sh.in
Source14:       create-tar.sh
# Gecko/Toolkit
Patch1:         toolkit-download-folder.patch
Patch2:         mozilla-nongnome-proxies.patch
Patch3:         mozilla-prefer_plugin_pref.patch
Patch4:         mozilla-shared-nss-db.patch
Patch5:         mozilla-kde.patch
Patch6:         mozilla-preferences.patch
Patch7:         mozilla-language.patch
Patch8:         mozilla-ntlm-full-path.patch
Patch9:         mozilla-repo.patch
Patch10:        mozilla-dump_syms-static.patch
Patch11:        mozilla-sle11.patch
Patch12:        mozilla-linux3.patch
Patch13:        mozilla-a11y.patch
# Firefox/browser
Patch31:        firefox-browser-css.patch
Patch32:        firefox-cross-desktop.patch
Patch33:        firefox-kde.patch
Patch34:        firefox-kde-114.patch
Patch38:        firefox-no-default-ualocale.patch
Patch39:        firefox-multilocale-chrome.patch
Patch41:        firefox-branded-icons.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires(post):   coreutils shared-mime-info desktop-file-utils
Requires(postun): shared-mime-info desktop-file-utils
Requires:       mozilla-nspr >= %(rpm -q --queryformat '%{VERSION}' mozilla-nspr)
Requires:       mozilla-nss >= %(rpm -q --queryformat '%{VERSION}' mozilla-nss)
Requires:       %{name}-branding > 4.0
%define firefox_appid \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%define _use_internal_dependency_generator 0
%define __find_requires sh %{SOURCE4}
%global provfind sh -c "grep -v '.so' | %__find_provides"
%global __find_provides %provfind
%define progname firefox
%define progdir %{_prefix}/%_lib/%{progname}
%define gnome_dir     %{_prefix}
%if %suse_version > 1130
%define desktop_file_name firefox
%else
%define desktop_file_name %{name}
%endif
### build options
%define branding 1
%define localize 1
%ifarch ppc ppc64 s390 s390x ia64 %arm
%define crashreporter    0
%else
%define crashreporter    1
%endif
### build options end

%description
Mozilla Firefox is a standalone web browser, designed for standards
compliance and performance.  Its functionality can be enhanced via a
plethora of extensions.

%package devel
Summary:        Devel package for Firefox
Group:          Development/Tools/Other
Provides:       firefox-devel = %{version}-%{release}
Requires:       %{name} = %{version}
Requires:       perl(XML::Simple)
Requires:       perl(Archive::Zip)

%description devel
Development files for Firefox to make packaging of addons easier.

%if %localize

%package translations-common
Summary:        Common translations for MozillaFirefox
Group:          System/Localization
Provides:       locale(%{name}:ar;ca;cs;da;de;en_GB;es_AR;es_CL;es_ES;fi;fr;hu;it;ja;ko;nb_NO;nl;pl;pt_BR;pt_PT;ru;sv_SE;zh_CN;zh_TW)
Requires:       %{name} = %{version}
Obsoletes:      %{name}-translations < %{version}-%{release}

%description translations-common
This package contains several common languages for the user interface
of MozillaFirefox.

%package translations-other
Summary:        Extra translations for MozillaFirefox
Group:          System/Localization
Provides:       locale(%{name}:af;ak;ast;be;bg;bn_BD;bn_IN;br;bs;cy;el;en_ZA;eo;es_MX;et;eu;fa;fy_NL;ga_IE;gd;gl;gu_IN;he;hi_IN;hr;hy_AM;id;is;kk;kn;ku;lg;lt;lv;mai;mk;ml;mr;nn_NO;nso;or;pa_IN;rm;ro;si;sk;sl;son;sq;sr;ta;ta_LK;te;th;tr;uk;vi;zu)
Requires:       %{name} = %{version}
Obsoletes:      %{name}-translations < %{version}-%{release}

%description translations-other
This package contains rarely used languages for the user interface
of MozillaFirefox.
%endif

%package branding-upstream
Summary:        Upstream branding for MozillaFirefox
Group:          Productivity/Networking/Web/Browsers
Provides:       %{name}-branding = 5.0
Conflicts:      otherproviders(%{name}-branding)
Supplements:    packageand(%{name}:branding-upstream)
#BRAND: Provide three files -
#BRAND: /usr/lib/firefox/browserconfig.properties that contains the
#BRAND: default homepage and some other default configuration options
#BRAND: /usr/lib/firefox/defaults/profile/bookmarks.html that contains
#BRAND: the list of default bookmarks
#BRAND: It's also possible to create a file
#BRAND: /usr/lib/firefox/defaults/preferences/firefox-$vendor.js to set
#BRAND: custom preference overrides.
#BRAND: It's also possible to drop files in /usr/lib/firefox/searchplugins

%description branding-upstream
This package provides upstream look and feel for MozillaFirefox.


%if %crashreporter

%package buildsymbols
Summary:        Breakpad buildsymbols for %{name}
Group:          Development/Debug

%description buildsymbols
This subpackage contains the Breakpad created and compatible debugging
symbols meant for upload to Mozilla's crash collector database.
%endif

%prep
%setup -q -n mozilla -b 7 -b 10
cd $RPM_BUILD_DIR/mozilla
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
#%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%if %suse_version < 1120
%patch11 -p1
%endif
%patch12 -p1
%patch13 -p1
#
%patch31 -p1
%patch32 -p1
%if %suse_version >= 1110
#%patch33 -p1
%endif
%if %suse_version >= 1140
#%patch34 -p1
%endif
%patch38 -p1
%patch39 -p1
%patch41 -p1

%build
# no need to add build time to binaries
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find . -regex ".*\.c\|.*\.cpp\|.*\.h" -exec sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" {} +
#
#kdehelperversion=$(cat toolkit/xre/nsKDEUtils.cpp | grep '#define KMOZILLAHELPER_VERSION' | cut -d ' ' -f 3)
#if test "$kdehelperversion" != %{kde_helper_version}; then
#  echo fix kde helper version in the .spec file
#  exit 1
#fi
source %{SOURCE5}
export MOZ_SOURCE_STAMP=$REV
export SOURCE_REPO=$REPO
export MOZ_SOURCE_REPO=$REPO
export MOZ_BUILD_DATE=%{releasedate}
export MOZILLA_OFFICIAL=1
export BUILD_OFFICIAL=1
export MOZ_TELEMETRY_REPORTING=1
export CFLAGS="$RPM_OPT_FLAGS -Os -fno-strict-aliasing"
%ifarch ppc64
export CFLAGS="$CFLAGS -mminimal-toc"
%endif
export CXXFLAGS="$CFLAGS"
export MOZCONFIG=$RPM_BUILD_DIR/mozconfig
cat << EOF > $MOZCONFIG
mk_add_options MOZILLA_OFFICIAL=1
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZ_MAKE_FLAGS=%{?jobs:-j%jobs}
mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/../obj
. \$topsrcdir/browser/config/mozconfig
ac_add_options --prefix=%{_prefix}
ac_add_options --libdir=%{_libdir}
ac_add_options --sysconfdir=%{_sysconfdir}
ac_add_options --mandir=%{_mandir}
ac_add_options --includedir=%{_includedir}
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-l10n-base=$RPM_BUILD_DIR/l10n
#ac_add_options --with-system-jpeg    # libjpeg-turbo is used internally
#ac_add_options --with-system-png     # doesn't work because of missing APNG support
ac_add_options --with-system-zlib
ac_add_options --disable-installer
ac_add_options --disable-updater
ac_add_options --disable-tests
ac_add_options --disable-debug
ac_add_options --enable-startup-notification
#ac_add_options --enable-chrome-format=jar
ac_add_options --enable-update-channel=beta
EOF
%if %suse_version > 1130
cat << EOF >> $MOZCONFIG
ac_add_options --disable-gnomevfs
ac_add_options --enable-gio
EOF
%endif
%if %branding
cat << EOF >> $MOZCONFIG
ac_add_options --enable-official-branding
EOF
%endif
%if %suse_version > 1110
cat << EOF >> $MOZCONFIG
ac_add_options --enable-libproxy
EOF
%endif
%if ! %crashreporter
cat << EOF >> $MOZCONFIG
ac_add_options --disable-crashreporter
EOF
%endif
make -f client.mk build

%install
cd $RPM_BUILD_DIR/obj
rm dist/bin/defaults/pref/firefox-l10n.js
source %{SOURCE5}
export MOZ_SOURCE_STAMP=$REV
export MOZ_SOURCE_REPO=$REPO
make -C browser/installer STRIP=/bin/true
# copy tree into RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{progdir}
cp -rf $RPM_BUILD_DIR/obj/dist/firefox/* $RPM_BUILD_ROOT%{progdir}
mkdir -p $RPM_BUILD_ROOT/%{progdir}/distribution/extensions
mkdir -p $RPM_BUILD_ROOT%{progdir}/searchplugins
# install kde.js
%if %suse_version >= 1110
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{progdir}/defaults/pref/kde.js
# make sure that instantApply is true by default
# (TODO: mozilla-kde.patch needs to be improved to really not load kde.js in non-KDE envs)
echo 'pref("browser.preferences.instantApply", true);' > $RPM_BUILD_ROOT%{progdir}/defaults/pref/firefox.js
%endif
# install add-plugins.sh
sed "s:%%PROGDIR:%{progdir}:g" \
  %{SOURCE13} > $RPM_BUILD_ROOT%{progdir}/add-plugins.sh
chmod 755 $RPM_BUILD_ROOT%{progdir}/add-plugins.sh
# install additional locales
%if %localize
rm -f %{_tmppath}/translations.*
touch %{_tmppath}/translations.{common,other}
for locale in $(awk '{ print $1; }' ../mozilla/browser/locales/shipped-locales); do
  case $locale in
   ja-JP-mac|en-US)
	;;
   *)
   	pushd $RPM_BUILD_DIR/compare-locales
	PYTHONPATH=lib \
	  scripts/compare-locales -m ../l10n-merged/$locale \
	  ../mozilla/browser/locales/l10n.ini ../l10n $locale
	popd
	LOCALE_MERGEDIR=$RPM_BUILD_DIR/l10n-merged/$locale \
  	make -C browser/locales langpack-$locale
	cp -rL dist/xpi-stage/locale-$locale \
	       $RPM_BUILD_ROOT%{progdir}/extensions/langpack-$locale@firefox.mozilla.org
	# remove prefs and profile defaults from langpack
	rm -rf $RPM_BUILD_ROOT%{progdir}/extensions/langpack-$locale@firefox.mozilla.org/defaults
	# check against the fixed common list and sort into the right filelist
	_matched=0
	for _match in ar ca cs da de en-GB es-AR es-CL es-ES fi fr hu it ja ko nb-NO nl pl pt-BR pt-PT ru sv-SE zh-CN zh-TW; do
	  [ "$_match" = "$locale" ] && _matched=1
	done
	[ $_matched -eq 1 ] && _l10ntarget=common || _l10ntarget=other
  	echo %{progdir}/extensions/langpack-$locale@firefox.mozilla.org \
	  >> %{_tmppath}/translations.$_l10ntarget
  esac
done
%endif
# remove some executable permissions
find $RPM_BUILD_ROOT%{progdir} \
     -name "*.js" -o \
     -name "*.jsm" -o \
     -name "*.rdf" -o \
     -name "*.properties" -o \
     -name "*.dtd" -o \
     -name "*.txt" -o \
     -name "*.xml" -o \
     -name "*.css" | xargs chmod a-x
# overwrite the mozilla start-script and link it to /usr/bin
mkdir --parents $RPM_BUILD_ROOT/usr/bin
sed "s:%%PREFIX:%{_prefix}:g
s:%%PROGDIR:%{progdir}:g
s:%%APPNAME:firefox:g
s:%%PROFILE:.mozilla/firefox:g" \
  %{SOURCE3} > $RPM_BUILD_ROOT%{progdir}/%{progname}.sh
chmod 755 $RPM_BUILD_ROOT%{progdir}/%{progname}.sh
ln -sf ../..%{progdir}/%{progname}.sh $RPM_BUILD_ROOT%{_bindir}/%{progname}
# desktop definition
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
install -m 644 %{SOURCE1} \
   $RPM_BUILD_ROOT%{_datadir}/applications/%{desktop_file_name}.desktop
# additional mime-types
mkdir -p $RPM_BUILD_ROOT%{_datadir}/mime/packages
cp %{SOURCE8} $RPM_BUILD_ROOT%{_datadir}/mime/packages/%{progname}.xml
# install man-page
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1/
cp %{SOURCE11} $RPM_BUILD_ROOT%{_mandir}/man1/%{progname}.1
##########
# ADDONS
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/mozilla/extensions/%{firefox_appid}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/mozilla/extensions/%{firefox_appid}
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps/
ln -sf %{progdir}/icons/mozicon128.png $RPM_BUILD_ROOT/usr/share/pixmaps/%{progname}.png
ln -sf %{progdir}/icons/mozicon128.png $RPM_BUILD_ROOT/usr/share/pixmaps/%{progname}-gnome.png
%if %branding
for size in 16 22 24 32 48 256; do
%else
for size in 16 32 48; do
%endif
  mkdir -p $RPM_BUILD_ROOT%{gnome_dir}/share/icons/hicolor/${size}x${size}/apps/
  ln -sf %{progdir}/chrome/icons/default/default$size.png \
         $RPM_BUILD_ROOT%{gnome_dir}/share/icons/hicolor/${size}x${size}/apps/%{progname}.png
done
%suse_update_desktop_file %{desktop_file_name} Network WebBrowser GTK
# excludes
rm -f $RPM_BUILD_ROOT%{progdir}/updater.ini
rm -f $RPM_BUILD_ROOT%{progdir}/removed-files
rm -f $RPM_BUILD_ROOT%{progdir}/README.txt
rm -f $RPM_BUILD_ROOT%{progdir}/old-homepage-default.properties
rm -f $RPM_BUILD_ROOT%{progdir}/run-mozilla.sh
rm -f $RPM_BUILD_ROOT%{progdir}/LICENSE
rm -f $RPM_BUILD_ROOT%{progdir}/precomplete
rm -f $RPM_BUILD_ROOT%{progdir}/dictionaries/en-US*
rm -f $RPM_BUILD_ROOT%{progdir}/firefox
# devel
mkdir -p %{buildroot}%{_bindir}
install -m 755 %SOURCE12 %{buildroot}%{_bindir}
# inspired by mandriva
mkdir -p %{buildroot}/etc/rpm
cat <<'FIN' >%{buildroot}/etc/rpm/macros.%{progname}
# Macros from %{name} package
%%firefox_major              %{major}
%%firefox_version            %{version}
%%firefox_mainver            %{mainver}
%%firefox_mozillapath        %%{_libdir}/%{progname}
%%firefox_pluginsdir         %%{_libdir}/browser-plugins
%%firefox_appid              \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%%firefox_extdir             %%(if [ "%%_target_cpu" = "noarch" ]; then echo %%{_datadir}/mozilla/extensions/%%{firefox_appid}; else echo %%{_libdir}/mozilla/extensions/%%{firefox_appid}; fi)

%%firefox_ext_install() \
   extdir="%%{buildroot}%%{firefox_extdir}/`mozilla-get-app-id '%%1'`" \
   mkdir -p "$extdir" \
   %%{__unzip} -q -d "$extdir" "%%1" \
   %%{nil}
FIN
# just dumping an xpi file there doesn't work...
#%%firefox_ext_install() \
#       extdir="%%{buildroot}%%{firefox_extdir}" \
#       mkdir -p "$extdir" \
#       cp "%%1" "$extdir" \
#       %%{nil}
# fdupes
%fdupes $RPM_BUILD_ROOT%{progdir}
%fdupes $RPM_BUILD_ROOT%{_datadir}
# create breakpad debugsymbols
%if %crashreporter
SYMBOLS_NAME="firefox-%{version}-%{release}.%{_arch}-%{suse_version}-symbols"
make buildsymbols \
  SYMBOL_INDEX_NAME="$SYMBOLS_NAME.txt" \
  SYMBOL_FULL_ARCHIVE_BASENAME="$SYMBOLS_NAME-full" \
  SYMBOL_ARCHIVE_BASENAME="$SYMBOLS_NAME"
if [ -e dist/*symbols.zip ]; then
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/mozilla/
  cp dist/*symbols.zip $RPM_BUILD_ROOT%{_datadir}/mozilla/
fi
%endif

%clean
rm -rf $RPM_BUILD_ROOT
%if %localize
rm -rf %{_tmppath}/translations.*
%endif

%post
# update mime and desktop database
%if %suse_version > 1130
%mime_database_post
%desktop_database_post
%icon_theme_cache_post
%else
if [ -f usr/bin/update-mime-database ] ; then
  usr/bin/update-mime-database %{_datadir}/mime > /dev/null || :
fi
if [ -f usr/bin/update-desktop-database ] ; then
  usr/bin/update-desktop-database > /dev/null || :
fi
%endif
%{progdir}/add-plugins.sh > /dev/null 2>&1
exit 0

%postun
%if %suse_version > 1130
%icon_theme_cache_postun
%desktop_database_postun
%mime_database_postun
%else
if [ -f usr/bin/update-mime-database ] ; then
  usr/bin/update-mime-database %{_datadir}/mime > /dev/null || :
fi
if [ -f usr/bin/update-desktop-database ] ; then
  usr/bin/update-desktop-database > /dev/null || :
fi
%endif
exit 0

%posttrans
[ -e %{progdir}/add-plugins.sh ] && \
  %{progdir}/add-plugins.sh > /dev/null 2>&1
exit 0

%preun
rm -f %{progdir}/dictionaries/*
exit 0

%files
%defattr(-,root,root)
%dir %{progdir}
%dir %{progdir}/chrome/
%dir %{progdir}/distribution/
%{progdir}/chrome/icons
%{progdir}/components/
%{progdir}/defaults/
%{progdir}/dictionaries/
%dir %{progdir}/extensions/
%{progdir}/distribution/extensions/
%{progdir}/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}
%{progdir}/icons/
%{progdir}/searchplugins/
%attr(755,root,root) %{progdir}/%{progname}.sh
%{progdir}/firefox-bin
%{progdir}/add-plugins.sh
%{progdir}/application.ini
%{progdir}/blocklist.xml
%{progdir}/dependentlibs.list
%{progdir}/*.so
%{progdir}/mozilla-xremote-client
%{progdir}/omni.ja
%{progdir}/platform.ini
%{progdir}/plugin-container
%if %crashreporter
%{progdir}/crashreporter-override.ini
%{progdir}/crashreporter
%{progdir}/crashreporter.ini
%{progdir}/Throbber-small.gif
%endif
%{progdir}/chrome.manifest
%{_datadir}/applications/%{desktop_file_name}.desktop
%{_datadir}/mime/packages/%{progname}.xml
%{_datadir}/pixmaps/firefox*
%dir %{_datadir}/mozilla
%dir %{_datadir}/mozilla/extensions
%dir %{_datadir}/mozilla/extensions/%{firefox_appid}
%dir %{_libdir}/mozilla
%dir %{_libdir}/mozilla/extensions
%dir %{_libdir}/mozilla/extensions/%{firefox_appid}
%{gnome_dir}/share/icons/hicolor/
%{_bindir}/%{progname}
%doc %{_mandir}/man1/%{progname}.1.gz

%files devel
%defattr(-,root,root)
%{_bindir}/mozilla-get-app-id
%config /etc/rpm/macros.%{progname}

%if %localize

%files translations-common -f %{_tmppath}/translations.common
%defattr(-,root,root)
%dir %{progdir}
%dir %{progdir}/extensions/

%files translations-other -f %{_tmppath}/translations.other
%defattr(-,root,root)
%dir %{progdir}
%dir %{progdir}/extensions/
%endif

# this package does not need to provide files but is needed to fulfill
# requirements if no other branding package is to be installed

%files branding-upstream
%defattr(-,root,root)
%dir %{progdir}

%if %crashreporter

%files buildsymbols
%defattr(-,root,root)
%{_datadir}/mozilla/*.zip
%endif

%changelog
