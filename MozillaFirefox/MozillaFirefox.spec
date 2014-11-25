#
# spec file for package MozillaFirefox
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#               2006-2014 Wolfgang Rosenauer
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


# changed with every update
%define major 33
%define mainver %major.99
%define update_channel beta
%define releasedate 2014112000

# general build definitions
%define firefox_appid \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%define _use_internal_dependency_generator 0
%define __find_requires sh %{SOURCE4}
%global provfind sh -c "grep -v '.so' | %__find_provides"
%global __find_provides %provfind
%define progname firefox
%define progdir %{_prefix}/%_lib/%{progname}
%define gnome_dir     %{_prefix}
%if 0%{?suse_version} > 1130
%define desktop_file_name firefox
%else
%define desktop_file_name %{name}
%endif
%if 0%{?suse_version} > 1210
%if 0%{?suse_version} > 1310
%define gstreamer_ver 1.0
%define gstreamer 1
%else
%define gstreamer_ver 0.10
%endif
%endif
# Set up Google API keys, see http://www.chromium.org/developers/how-tos/api-keys
# Note: these are for the openSUSE Firefox builds ONLY. For your own distribution,
# please get your own set of keys.
%define _google_api_key AIzaSyD1hTe85_a14kr1Ks8T3Ce75rvbR1_Dx7Q
%define branding 1
%define localize 1
%ifarch aarch64 ppc ppc64 ppc64le s390 s390x ia64 %arm
%define crashreporter 0
%else
%define crashreporter 1
%endif

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
BuildRequires:  makeinfo
BuildRequires:  python-devel
BuildRequires:  startup-notification-devel
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-libXt-devel
BuildRequires:  yasm
BuildRequires:  zip
%if 0%{?suse_version} > 1110
BuildRequires:  libiw-devel
BuildRequires:  libproxy-devel
%else
BuildRequires:  wireless-tools
%endif
BuildRequires:  mozilla-nspr-devel >= 4.10.7
BuildRequires:  mozilla-nss-devel >= 3.17.2
BuildRequires:  nss-shared-helper-devel
BuildRequires:  pkgconfig(libpulse)
%if 0%{?suse_version} > 1210
BuildRequires:  pkgconfig(gstreamer-%gstreamer_ver)
BuildRequires:  pkgconfig(gstreamer-app-%gstreamer_ver)
BuildRequires:  pkgconfig(gstreamer-plugins-base-%gstreamer_ver)
%if 0%{?gstreamer} == 1
Requires:       libgstreamer-1_0-0
Recommends:     gstreamer-fluendo-mp3
Recommends:     gstreamer-plugins-libav
%else
Requires:       libgstreamer-0_10-0
Recommends:     gstreamer-0_10-fluendo-mp3
Recommends:     gstreamer-0_10-plugins-ffmpeg
%endif
%endif
Version:        %{mainver}
Release:        0
Provides:       firefox = %{mainver}
Provides:       firefox = %{version}-%{release}
Provides:       web_browser
Provides:       browser(npapi)
# this is needed to match this package with the kde4 helper package without the main package
# having a hard requirement on the kde4 package
%define kde_helper_version 6
Provides:       mozilla-kde4-version = %{kde_helper_version}
Summary:        Mozilla Firefox Web Browser
License:        MPL-2.0
Group:          Productivity/Networking/Web/Browsers
Url:            http://www.mozilla.org/
Source:         firefox-%{version}-source.tar.xz
Source1:        MozillaFirefox.desktop
Source2:        MozillaFirefox-rpmlintrc
Source3:        mozilla.sh.in
Source4:        find-external-requires.sh
Source5:        source-stamp.txt
Source6:        kde.js
Source7:        l10n-%{version}.tar.xz
Source8:        firefox-mimeinfo.xml
Source9:        firefox.js
Source10:       compare-locales.tar.xz
Source11:       firefox.1
Source12:       mozilla-get-app-id
Source13:       spellcheck.js
Source14:       create-tar.sh
Source15:       firefox-appdata.xml
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
Patch10:        mozilla-sle11.patch
Patch11:        mozilla-icu-strncat.patch
Patch12:        mozilla-arm-disable-edsp.patch
Patch13:        mozilla-bmo1088588.patch
# Firefox/browser
Patch101:       firefox-kde.patch
Patch102:       firefox-kde-114.patch
Patch103:       firefox-no-default-ualocale.patch
Patch104:       firefox-multilocale-chrome.patch
Patch105:       firefox-branded-icons.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires(post):   coreutils shared-mime-info desktop-file-utils
Requires(postun): shared-mime-info desktop-file-utils
Requires:       %{name}-branding > 20.0
Requires:       mozilla-nspr >= %(rpm -q --queryformat '%{VERSION}' mozilla-nspr)
Requires:       mozilla-nss >= %(rpm -q --queryformat '%{VERSION}' mozilla-nss)
Recommends:     libcanberra0
Recommends:     libpulse0
# libproxy's mozjs pacrunner crashes FF (bnc#759123)
%if 0%{?suse_version} < 1220
Obsoletes:      libproxy1-pacrunner-mozjs <= 0.4.7
%endif

%description
Mozilla Firefox is a standalone web browser, designed for standards
compliance and performance.  Its functionality can be enhanced via a
plethora of extensions.

%package devel
Summary:        Devel package for Firefox
Group:          Development/Tools/Other
Provides:       firefox-devel = %{version}-%{release}
Requires:       %{name} = %{version}
Requires:       perl(Archive::Zip)
Requires:       perl(XML::Simple)

%description devel
Development files for Firefox to make packaging of addons easier.

%if %localize
%package translations-common
Summary:        Common translations for Firefox
Group:          System/Localization
Provides:       locale(%{name}:ar;ca;cs;da;de;en_GB;el;es_AR;es_CL;es_ES;fi;fr;hu;it;ja;ko;nb_NO;nl;pl;pt_BR;pt_PT;ru;sv_SE;zh_CN;zh_TW)
Requires:       %{name} = %{version}
Obsoletes:      %{name}-translations < %{version}-%{release}

%description translations-common
This package contains several common languages for the user interface
of Firefox.

%package translations-other
Summary:        Extra translations for Firefox
Group:          System/Localization
Provides:       locale(%{name}:ach;af;ak;as;ast;be;bg;bn_BD;bn_IN;br;bs;csb;cy;en_ZA;eo;es_MX;et;eu;fa;ff;fy_NL;ga_IE;gd;gl;gu_IN;he;hi_IN;hr;hy_AM;id;is;kk;km;kn;ku;lg;lij;lt;lv;mai;mk;ml;mr;nn_NO;nso;or;pa_IN;rm;ro;si;sk;sl;son;sq;sr;ta;ta_LK;te;th;tr;uk;vi;zu)
Requires:       %{name} = %{version}
Obsoletes:      %{name}-translations < %{version}-%{release}

%description translations-other
This package contains rarely used languages for the user interface
of Firefox.
%endif

%package branding-upstream
Summary:        Upstream branding for Firefox
Group:          Productivity/Networking/Web/Browsers
Provides:       %{name}-branding = %{version}
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
This package provides upstream look and feel for Firefox.


%if %crashreporter

%package buildsymbols
Summary:        Breakpad buildsymbols for %{name}
Group:          Development/Debug

%description buildsymbols
This subpackage contains the Breakpad created and compatible debugging
symbols meant for upload to Mozilla's crash collector database.
%endif

%prep
%if %localize
%setup -q -n mozilla -b 7 -b 10
%else
%setup -q -n mozilla
%endif
cd $RPM_BUILD_DIR/mozilla
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%if 0%{?suse_version} < 1120
%patch10 -p1
%endif
%patch11 -p1
%patch12 -p1
%patch13 -p1
# Firefox
%patch101 -p1
%if 0%{?suse_version} >= 1140
%patch102 -p1
%endif
%patch103 -p1
%patch104 -p1
%patch105 -p1

%build
# no need to add build time to binaries
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find . -regex ".*\.c\|.*\.cpp\|.*\.h" -exec sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" {} +
#
kdehelperversion=$(cat toolkit/xre/nsKDEUtils.cpp | grep '#define KMOZILLAHELPER_VERSION' | cut -d ' ' -f 3)
if test "$kdehelperversion" != %{kde_helper_version}; then
  echo fix kde helper version in the .spec file
  exit 1
fi
source %{SOURCE5}
export MOZ_SOURCE_STAMP=$REV
export SOURCE_REPO=$REPO
export source_repo=$REPO
export MOZ_SOURCE_REPO=$REPO
export MOZ_BUILD_DATE=%{releasedate}
export MOZILLA_OFFICIAL=1
export BUILD_OFFICIAL=1
export MOZ_TELEMETRY_REPORTING=1
export MOZ_GOOGLE_API_KEY=%{_google_api_key}
export CFLAGS="%{optflags} -fno-strict-aliasing"
%ifarch %arm
export CFLAGS="${CFLAGS/-g / }"
%endif
%ifarch %arm %ix86
# Limit RAM usage during link
export LDFLAGS="${LDFLAGS} -Wl,--no-keep-memory -Wl,--reduce-memory-overheads"
%endif
%ifarch ppc64 ppc64le
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
ac_add_options --enable-release
ac_add_options --enable-stdcxx-compat
%ifarch %ix86 %arm
%if 0%{?suse_version} > 1230
ac_add_options --disable-optimize
%endif
%endif
%ifnarch ppc ppc64 ppc64le aarch64
ac_add_options --enable-elf-hack
%endif
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
%if %{localize}
ac_add_options --with-l10n-base=$RPM_BUILD_DIR/l10n
%endif
#ac_add_options --with-system-jpeg    # libjpeg-turbo is used internally
#ac_add_options --with-system-png     # doesn't work because of missing APNG support
ac_add_options --with-system-zlib
ac_add_options --disable-installer
ac_add_options --disable-updater
ac_add_options --disable-tests
ac_add_options --disable-debug
ac_add_options --enable-startup-notification
#ac_add_options --enable-chrome-format=jar
ac_add_options --enable-update-channel=%{update_channel}
%if 0%{?gstreamer} == 1
ac_add_options --enable-gstreamer=1.0
%endif
%if 0%{?suse_version} > 1130
ac_add_options --disable-gnomevfs
ac_add_options --enable-gio
%endif
%if 0%{?suse_version} < 1220
ac_add_options --disable-gstreamer
%endif
%if %branding
ac_add_options --enable-official-branding
%endif
%if 0%{?suse_version} > 1110
ac_add_options --enable-libproxy
%endif
%if ! %crashreporter
ac_add_options --disable-crashreporter
%endif
# Disable neon for arm as it does not build correctly
%ifarch %arm
ac_add_options --disable-neon
%endif
%ifnarch %ix86 x86_64
ac_add_options --disable-webrtc
%endif
# try to use OpenGL-ES on ARM
%ifarch %arm aarch64
ac_add_options --with-gl-provider=EGL
%endif
EOF
make -f client.mk build

%install
cd $RPM_BUILD_DIR/obj
source %{SOURCE5}
export MOZ_SOURCE_STAMP=$REV
export MOZ_SOURCE_REPO=$REPO
# need to remove default en-US firefox-l10n.js before it gets
# populated into browser's omni.ja; it only contains general.useragent.locale
# which should be loaded from each language pack (set in firefox.js)
rm dist/bin/browser/defaults/preferences/firefox-l10n.js
make -C browser/installer STRIP=/bin/true MOZ_PKG_FATAL_WARNINGS=0
#DEBUG (break the build if searchplugins are missing / temporary)
grep amazondotcom dist/firefox/browser/omni.ja
# copy tree into RPM_BUILD_ROOT
mkdir -p %{buildroot}%{progdir}
cp -rf $RPM_BUILD_DIR/obj/dist/firefox/* %{buildroot}%{progdir}
mkdir -p %{buildroot}%{progdir}/distribution/extensions
mkdir -p %{buildroot}%{progdir}/browser/searchplugins
mkdir -p %{buildroot}%{progdir}/browser/defaults/preferences/
# install gre prefs
install -m 644 %{SOURCE13} %{buildroot}%{progdir}/defaults/pref/
# install browser prefs
install -m 644 %{SOURCE6} %{buildroot}%{progdir}/browser/defaults/preferences/kde.js
install -m 644 %{SOURCE9} %{buildroot}%{progdir}/browser/defaults/preferences/firefox.js
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
	       %{buildroot}%{progdir}/browser/extensions/langpack-$locale@firefox.mozilla.org
	# remove prefs, profile defaults, and hyphenation from langpack
	rm -rf %{buildroot}%{progdir}/browser/extensions/langpack-$locale@firefox.mozilla.org/defaults
	rm -rf %{buildroot}%{progdir}/browser/extensions/langpack-$locale@firefox.mozilla.org/hyphenation
	# check against the fixed common list and sort into the right filelist
	_matched=0
	for _match in ar ca cs da de en-GB el es-AR es-CL es-ES fi fr hu it ja ko nb-NO nl pl pt-BR pt-PT ru sv-SE zh-CN zh-TW; do
	  [ "$_match" = "$locale" ] && _matched=1
	done
	[ $_matched -eq 1 ] && _l10ntarget=common || _l10ntarget=other
  	echo %{progdir}/browser/extensions/langpack-$locale@firefox.mozilla.org \
	  >> %{_tmppath}/translations.$_l10ntarget
  esac
done
%endif
# remove some executable permissions
find %{buildroot}%{progdir} \
     -name "*.js" -o \
     -name "*.jsm" -o \
     -name "*.rdf" -o \
     -name "*.properties" -o \
     -name "*.dtd" -o \
     -name "*.txt" -o \
     -name "*.xml" -o \
     -name "*.css" | xargs chmod a-x
# remove mkdir.done files from installed base
find %{buildroot}%{progdir} -name ".mkdir.done" | xargs rm
# overwrite the mozilla start-script and link it to /usr/bin
mkdir --parents %{buildroot}/usr/bin
sed "s:%%PREFIX:%{_prefix}:g
s:%%PROGDIR:%{progdir}:g
s:%%APPNAME:firefox:g
s:%%PROFILE:.mozilla/firefox:g" \
  %{SOURCE3} > %{buildroot}%{progdir}/%{progname}.sh
chmod 755 %{buildroot}%{progdir}/%{progname}.sh
ln -sf ../..%{progdir}/%{progname}.sh %{buildroot}%{_bindir}/%{progname}
# desktop definition
mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE1} \
   %{buildroot}%{_datadir}/applications/%{desktop_file_name}.desktop
# additional mime-types
mkdir -p %{buildroot}%{_datadir}/mime/packages
cp %{SOURCE8} %{buildroot}%{_datadir}/mime/packages/%{progname}.xml
# appdata
mkdir -p %{buildroot}%{_datadir}/appdata
cp %{SOURCE15} %{buildroot}%{_datadir}/appdata/%{desktop_file_name}.appdata.xml
# install man-page
mkdir -p %{buildroot}%{_mandir}/man1/
cp %{SOURCE11} %{buildroot}%{_mandir}/man1/%{progname}.1
##########
# ADDONS
#
mkdir -p %{buildroot}%{_datadir}/mozilla/extensions/%{firefox_appid}
mkdir -p %{buildroot}%{_libdir}/mozilla/extensions/%{firefox_appid}
mkdir -p %{buildroot}/usr/share/pixmaps/
ln -sf %{progdir}/browser/icons/mozicon128.png %{buildroot}/usr/share/pixmaps/%{progname}.png
ln -sf %{progdir}/browser/icons/mozicon128.png %{buildroot}/usr/share/pixmaps/%{progname}-gnome.png
%if %branding
for size in 16 22 24 32 48 256; do
%else
for size in 16 32 48; do
%endif
  mkdir -p %{buildroot}%{gnome_dir}/share/icons/hicolor/${size}x${size}/apps/
  ln -sf %{progdir}/browser/chrome/icons/default/default$size.png \
         %{buildroot}%{gnome_dir}/share/icons/hicolor/${size}x${size}/apps/%{progname}.png
done
%suse_update_desktop_file %{desktop_file_name} Network WebBrowser GTK
# excludes
rm -f %{buildroot}%{progdir}/updater.ini
rm -f %{buildroot}%{progdir}/removed-files
rm -f %{buildroot}%{progdir}/README.txt
rm -f %{buildroot}%{progdir}/old-homepage-default.properties
rm -f %{buildroot}%{progdir}/run-mozilla.sh
rm -f %{buildroot}%{progdir}/LICENSE
rm -f %{buildroot}%{progdir}/precomplete
rm -f %{buildroot}%{progdir}/dictionaries/en-US*
rm -f %{buildroot}%{progdir}/update-settings.ini
# devel
mkdir -p %{buildroot}%{_bindir}
install -m 755 %SOURCE12 %{buildroot}%{_bindir}
# inspired by mandriva
mkdir -p %{buildroot}%{_sysconfdir}/rpm
cat <<'FIN' >%{buildroot}%{_sysconfdir}/rpm/macros.%{progname}
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
%fdupes %{buildroot}%{progdir}
%fdupes %{buildroot}%{_datadir}
# create breakpad debugsymbols
%if %crashreporter
SYMBOLS_NAME="firefox-%{version}-%{release}.%{_arch}-%{suse_version}-symbols"
make buildsymbols \
  SYMBOL_INDEX_NAME="$SYMBOLS_NAME.txt" \
  SYMBOL_FULL_ARCHIVE_BASENAME="$SYMBOLS_NAME-full" \
  SYMBOL_ARCHIVE_BASENAME="$SYMBOLS_NAME"
if [ -e dist/*symbols.zip ]; then
  mkdir -p %{buildroot}%{_datadir}/mozilla/
  cp dist/*symbols.zip %{buildroot}%{_datadir}/mozilla/
fi
%endif

%clean
rm -rf %{buildroot}
%if %localize
rm -rf %{_tmppath}/translations.*
%endif

%post
# update mime and desktop database
%if 0%{?suse_version} > 1130
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
exit 0

%postun
%if 0%{?suse_version} > 1130
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

%files
%defattr(-,root,root)
%dir %{progdir}
%dir %{progdir}/browser/
%dir %{progdir}/browser/chrome/
%dir %{progdir}/browser/extensions/
%{progdir}/browser/components/
%{progdir}/browser/defaults
%{progdir}/browser/icons/
%{progdir}/browser/chrome/icons
%{progdir}/browser/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}
%{progdir}/browser/searchplugins/
%{progdir}/browser/blocklist.xml
%{progdir}/browser/chrome.manifest
%{progdir}/browser/omni.ja
%dir %{progdir}/distribution/
%{progdir}/distribution/extensions/
%{progdir}/components/
%{progdir}/defaults/
%{progdir}/dictionaries/
%{progdir}/webapprt/
%attr(755,root,root) %{progdir}/%{progname}.sh
%{progdir}/firefox
%{progdir}/firefox-bin
%{progdir}/application.ini
%{progdir}/dependentlibs.list
%{progdir}/*.so
%{progdir}/mozilla-xremote-client
%{progdir}/omni.ja
%{progdir}/platform.ini
%{progdir}/plugin-container
%{progdir}/webapprt-stub
%{progdir}/chrome.manifest
%if %crashreporter
%{progdir}/crashreporter
%{progdir}/crashreporter.ini
%{progdir}/Throbber-small.gif
%{progdir}/browser/crashreporter-override.ini
%endif
%{_datadir}/applications/%{desktop_file_name}.desktop
%{_datadir}/mime/packages/%{progname}.xml
%{_datadir}/pixmaps/firefox*
%{_datadir}/appdata/
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
%config %{_sysconfdir}/rpm/macros.%{progname}

%if %localize

%files translations-common -f %{_tmppath}/translations.common
%defattr(-,root,root)
%dir %{progdir}
%dir %{progdir}/browser/extensions/

%files translations-other -f %{_tmppath}/translations.other
%defattr(-,root,root)
%dir %{progdir}
%dir %{progdir}/browser/extensions/
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
