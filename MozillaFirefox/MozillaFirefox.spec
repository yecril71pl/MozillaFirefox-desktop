#
# spec file for package MozillaFirefox (Version 4.0b)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
#               2006-2010 Wolfgang Rosenauer
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

# norootforbuild


Name:           MozillaFirefox
%define use_xulrunner 0
%define xulrunner mozilla-xulrunner20
BuildRequires:  autoconf213 gcc-c++ libcurl-devel libgnomeui-devel libidl-devel libnotify-devel python startup-notification-devel unzip pkg-config update-desktop-files zip fdupes Mesa-devel yasm hunspell-devel nss-shared-helper-devel
%if %suse_version > 1110
BuildRequires:  libiw-devel
BuildRequires:  libproxy-devel
%else
BuildRequires:  wireless-tools
%endif
%if 0%{?use_xulrunner}
BuildRequires:  %{xulrunner}-devel = 2.0b
%endif
License:        GPLv2+ ; LGPLv2.1+ ; MPLv1.1+
Provides:       web_browser
Provides:       firefox
Version:        4.0b
Release:        1
%define         releasedate 2010083100
Summary:        Mozilla Firefox Web Browser
Url:            http://www.mozilla.org/
Group:          Productivity/Networking/Web/Browsers
# this is needed to match this package with the kde4 helper package without the main package
# having a hard requirement on the kde4 package
%define kde_helper_version 6
Provides:       mozilla-kde4-version = %{kde_helper_version}
Source:         firefox-%{version}-source.tar.bz2
Source1:        MozillaFirefox.desktop
Source2:        MozillaFirefox-rpmlintrc
Source3:        mozilla.sh.in
Source4:        find-external-requires.sh
Source5:        firefox.schemas
Source6:        kde.js
Source7:        l10n-%{version}.tar.bz2
Source8:        firefox-mimeinfo.xml
Source9:        firefox-lockdown.js
Source10:       compare-locales.tar.bz2
Source11:       add-plugins.sh.in
Source12:       create-tar.sh
Source13:       toolkit-lockdown.js
Source16:       firefox.1
# Gecko/Toolkit
Patch1:         toolkit-download-folder.patch
Patch2:         mozilla-nongnome-proxies.patch
Patch3:         mozilla-prefer_plugin_pref.patch
Patch4:         mozilla-shared-nss-db.patch
Patch5:         mozilla-kde.patch
Patch6:         mozilla-gconf-backend.patch
Patch7:         gecko-lockdown.patch
Patch8:         toolkit-ui-lockdown.patch
Patch9:         mozilla-cpuid.patch
Patch10:        mozilla-buildsymbols.patch
Patch11:        mozilla-cairo-lcd.patch
# Firefox/browser
Patch30:        firefox-libxul-sdk.patch
Patch31:        firefox-credits.patch
Patch32:        firefox-linkorder.patch
Patch33:        firefox-browser-css.patch
Patch34:        firefox-cross-desktop.patch
Patch35:        firefox-appname.patch
Patch36:        firefox-kde.patch
Patch37:        firefox-ui-lockdown.patch
Patch38:        firefox-no-sync-l10n.patch
Patch39:        firefox-sync-system-nss.patch
Patch40:        firefox-sync-build.patch
Patch41:        firefox-tabview.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires(post):   coreutils shared-mime-info desktop-file-utils
Requires(postun): shared-mime-info desktop-file-utils
%if 0%{?use_xulrunner}
Requires:       %{xulrunner} >= %(rpm -q --queryformat '%{VERSION}-%{RELEASE}' %{xulrunner})
%requires_eq    %{xulrunner}
%ifarch %ix86
Requires:       %{xulrunner}-32bit >= %(rpm -q --queryformat '%{VERSION}-%{RELEASE}' %{xulrunner})
Requires:       %{xulrunner}-32bit = %(rpm -q --queryformat '%{VERSION}' %{xulrunner})
%endif
%endif
Requires:       %{name}-branding >= 4.0
%define _use_internal_dependency_generator 0
%define __find_requires sh %{SOURCE4}
%global provfind sh -c "grep -v '.so' | %__find_provides"
%global __find_provides %provfind
%define progname firefox
%define progdir %{_prefix}/%_lib/%{progname}
%define gnome_dir     %{_prefix}
### build options
%define branding 1
%define localize 1
%ifarch ppc ppc64 s390 s390x ia64
%define crashreporter    0
%define plugincontainer  0
%else
%define crashreporter    1
%define plugincontainer  1
%endif
### build options end

%description
Mozilla Firefox is a standalone web browser, designed for standards
compliance and performance.  Its functionality can be enhanced via a
plethora of extensions.


%if %localize
%package translations-common
Summary:        Common translations for MozillaFirefox
License:        GPLv2+ ; LGPLv2.1+ ; MPLv1.1+
Provides:       locale(%{name}:ar;ca;cs;da;de;en_GB;es_AR;es_CL;es_ES;fi;fr;hu;it;ja;ko;nb_NO;nl;pl;pt_BR;pt_PT;ru;sv_SE;zh_CN;zh_TW)
Group:          System/Localization
Requires:       %{name} = %{version}
%if 0%{?use_xulrunner}
Requires:       %{xulrunner}-translations-common
%endif
Obsoletes:      %{name}-translations < %{version}-%{release}

%description translations-common
This package contains several common languages for the user interface
of MozillaFirefox.

%package translations-other
Summary:        Extra translations for MozillaFirefox
License:        GPLv2+ ; LGPLv2.1+ ; MPLv1.1+
Provides:       locale(%{name}:af;as;be;bg;bn_BD;bn_IN;cy;el;eo;es_MX;et;eu;fa;fy_NL;ga_IE;gl;gu_IN;he;hi_IN;hr;id;is;ka;kk;kn;ku;lt;lv;mk;ml;mr;nn_NO;oc;or;pa_IN;rm;ro;si;sk;sl;sq;sr;ta;ta_LK;te;th;tr;uk;vi)
Group:          System/Localization
Requires:       %{name} = %{version}
%if 0%{?use_xulrunner}
Requires:       %{xulrunner}-translations-other
%endif
Obsoletes:      %{name}-translations < %{version}-%{release}

%description translations-other
This package contains rarely used languages for the user interface
of MozillaFirefox.

%endif

%package branding-upstream
License:        GPLv2+ ; LGPLv2.1+ ; MPLv1.1+
Summary:        Upstream branding for MozillaFirefox
Group:          Productivity/Networking/Web/Browsers
Provides:       %{name}-branding = 4.0
Conflicts:      otherproviders(%{name}-branding)
Supplements:    packageand(%{name}:branding-upstream)
#BRAND: Provide three files -
#BRAND: /usr/lib/firefox/browserconfig.properties that contains the
#BRAND: default homepage and some other default configuration options
#BRAND: /usr/lib/firefox/defaults/profile/bookmarks.html that contains
#BRAND: the list of default bookmarks
#BRAND: /etc/gconf/schemas/firefox.schemas
#BRAND: for mapping some Firefox prefs to gconf
#BRAND: It's also possible to create a file
#BRAND: /usr/lib/firefox/defaults/preferences/firefox-$vendor.js to set
#BRAND: custom preference overrides.
#BRAND: It's also possible to drop files in /usr/lib/firefox/searchplugins

%description branding-upstream
This package provides upstream look and feel for MozillaFirefox.

%if %crashreporter && !0%{?use_xulrunner}
%package buildsymbols
License:        GPLv2+ ; LGPLv2.1+ ; MPLv1.1+
Summary:        Breakpad buildsymbols for %{name}
Group:          Development/Debug

%description buildsymbols
This subpackage contains the Breakpad created and compatible debugging
symbols meant for upload to Mozilla's crash collector database.
%endif

%prep
%setup -q -n mozilla -b 7 -b 10
cd $RPM_BUILD_DIR/mozilla
# Gecko/Toolkit
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
#%patch6 -p1
#%patch7 -p1
#%patch8 -p1
%patch9 -p1
%patch10 -p1
#%patch11 -p1
# Firefox/browser
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%if %suse_version >= 1110
%patch36 -p1
# install kde.js
install -m 644 %{SOURCE6} browser/app/profile/kde.js
%endif
#%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1

%build
kdehelperversion=$(cat toolkit/xre/nsKDEUtils.cpp | grep '#define KMOZILLAHELPER_VERSION' | cut -d ' ' -f 3)
if test "$kdehelperversion" != %{kde_helper_version}; then
  echo fix kde helper version in the .spec file
  exit 1
fi
export MOZ_BUILD_DATE=%{releasedate}
export MOZILLA_OFFICIAL=1
export BUILD_OFFICIAL=1
export CFLAGS="$RPM_OPT_FLAGS -Os -fno-strict-aliasing"  
%ifarch ppc64
export CFLAGS="$CFLAGS -mminimal-toc"
%endif
export CXXFLAGS="$CFLAGS"
export MOZCONFIG=$RPM_BUILD_DIR/mozconfig
%if 0%{?use_xulrunner}
SDKDIR=$(pkg-config --variable=sdkdir libxul)
%endif
cat << EOF > $MOZCONFIG
mk_add_options MOZILLA_OFFICIAL=1
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZ_MILESTONE_RELEASE=1
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
ac_add_options --with-system-jpeg
#ac_add_options --with-system-png     # doesn't work because of missing APNG support
ac_add_options --with-system-zlib
ac_add_options --enable-startup-notification
ac_add_options --enable-system-hunspell
ac_add_options --disable-installer
ac_add_options --disable-updater
ac_add_options --disable-tests
ac_add_options --enable-update-channel=beta
#ac_add_options --enable-debug
EOF
%if 0%{?use_xulrunner}
cat << EOF >> $MOZCONFIG
ac_add_options --with-libxul-sdk=$SDKDIR
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
%if ! %plugincontainer
cat << EOF >> $MOZCONFIG
# Chromium IPC is not ported to Power,S/390 and Itanium (currently just x86,x86_64 and arm)
ac_add_options --disable-ipc
EOF
%endif
make -f client.mk build

%install
cd $RPM_BUILD_DIR/obj
# FIXME (will be needed once lockdown is integrated; needs omni.jar adoption)
#cp %{SOURCE9} dist/bin/defaults/preferences/lockdown.js
rm dist/bin/defaults/preferences/firefox-l10n.js
make -C browser/installer STRIP=/bin/true
# copy tree into RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{progdir}
cp -rf $RPM_BUILD_DIR/obj/dist/firefox/* $RPM_BUILD_ROOT/%{progdir}
# install additional locales
%if %localize
rm -f %{_tmppath}/translations.*
touch %{_tmppath}/translations.{common,other}
for locale in $(awk '{ print $1; }' browser/locales/shipped-locales); do
  case $locale in
   ja-JP-mac|en-US)
	;;
   *)
   	pushd $RPM_BUILD_DIR/compare-locales
	PYTHONPATH=lib \
	  scripts/compare-locales -m ../l10n-merged/$locale \
	  ../mozilla/browser/locales/l10n.ini ../l10n $locale
	popd
	LOCALE_MERGEDIR=../l10n-merged \
  	make -C browser/locales libs-$locale
  	cp dist/xpi-stage/locale-$locale/chrome/$locale.jar \
    	  $RPM_BUILD_ROOT%{progdir}/chrome
  	cp dist/xpi-stage/locale-$locale/chrome/$locale.manifest \
     	  $RPM_BUILD_ROOT%{progdir}/chrome
	# check against the fixed common list and sort into the right filelist
	_matched=0
	for _match in ar ca cs da de en-GB es-AR es-CL es-ES fi fr hu it ja ko nb-NO nl pl pt-BR pt-PT ru sv-SE zh-CN zh-TW; do
	  [ "$_match" = "$locale" ] && _matched=1
	done
	[ $_matched -eq 1 ] && _l10ntarget=common || _l10ntarget=other
  	echo %{progdir}/chrome/$locale.jar      >> %{_tmppath}/translations.$_l10ntarget
  	echo %{progdir}/chrome/$locale.manifest >> %{_tmppath}/translations.$_l10ntarget
  esac
done
%endif
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
   $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
# additional mime-types
mkdir -p $RPM_BUILD_ROOT%{_datadir}/mime/packages
cp %{SOURCE8} $RPM_BUILD_ROOT%{_datadir}/mime/packages/%{progname}.xml
# install man-page
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1/
cp %{SOURCE16} $RPM_BUILD_ROOT%{_mandir}/man1/%{progname}.1
##########
# ADDONS
#
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps/
ln -sf %{progdir}/icons/mozicon128.png $RPM_BUILD_ROOT/usr/share/pixmaps/%{progname}.png
ln -sf %{progdir}/icons/mozicon128.png $RPM_BUILD_ROOT/usr/share/pixmaps/%{progname}-gnome.png
%if %branding
for size in 16 32 48; do
  mkdir -p $RPM_BUILD_ROOT%{gnome_dir}/share/icons/hicolor/${size}x${size}/apps/
  ln -sf %{progdir}/chrome/icons/default/default$size.png \
         $RPM_BUILD_ROOT%{gnome_dir}/share/icons/hicolor/${size}x${size}/apps/%{progname}.png
done
%endif
%suse_update_desktop_file %{name} Network WebBrowser X-Ximian-Main X-Ximian-Toplevel GTK
# excludes
rm -f $RPM_BUILD_ROOT%{progdir}/updater.ini
rm -f $RPM_BUILD_ROOT%{progdir}/removed-files
rm -f $RPM_BUILD_ROOT%{progdir}/README.txt
rm -f $RPM_BUILD_ROOT%{progdir}/old-homepage-default.properties
rm -f $RPM_BUILD_ROOT%{progdir}/run-mozilla.sh
rm -f $RPM_BUILD_ROOT%{progdir}/LICENSE
# fdupes
%fdupes $RPM_BUILD_ROOT%{progdir}
%fdupes $RPM_BUILD_ROOT%{_datadir}
# create breakpad debugsymbols
%if %crashreporter && !0%{?use_xulrunner}
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
if [ -f usr/bin/update-mime-database ] ; then
  usr/bin/update-mime-database %{_datadir}/mime > /dev/null || :
fi
%if %suse_version >= 1030
if [ -f usr/bin/update-desktop-database ] ; then
  usr/bin/update-desktop-database > /dev/null || :
fi
%else
if [ -f opt/gnome/bin/update-mime-database ] ; then
  opt/gnome/bin/update-mime-database > /dev/null || :
fi
%endif
exit 0

%postun
if [ -f usr/bin/update-mime-database ] ; then
  usr/bin/update-mime-database %{_datadir}/mime > /dev/null || :
fi
%if %suse_version >= 1030
if [ -f usr/bin/update-desktop-database ] ; then
  usr/bin/update-desktop-database > /dev/null || :
fi
%else
if [ -f opt/gnome/bin/update-mime-database ] ; then
  opt/gnome/bin/update-mime-database > /dev/null || :
fi
%endif

%if !0%{?use_xulrunner}
%posttrans
[ -e %{_libdir}/firefox/add-plugins.sh ] && \
  %{_libdir}/firefox/add-plugins.sh > /dev/null 2>&1
exit 0
%endif

%files
%defattr(-,root,root)
%dir %{progdir}
%dir %{progdir}/chrome/
%{progdir}/chrome/icons
%{progdir}/components/
#%exclude %{progdir}/defaults/profile/bookmarks.html
%{progdir}/extensions/
%{progdir}/icons/
%{progdir}/searchplugins/
%attr(755,root,root) %{progdir}/%{progname}.sh
%{progdir}/firefox
%{progdir}/application.ini
%{progdir}/blocklist.xml
%{progdir}/omni.jar
%if %crashreporter
%{progdir}/crashreporter-override.ini
%endif
%{progdir}/chrome.manifest
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{progname}.xml
%{_datadir}/pixmaps/firefox*
%if %branding
%{gnome_dir}/share/icons/hicolor/
%endif
%{_bindir}/%{progname}
%doc %{_mandir}/man1/%{progname}.1.gz

%if %localize

%files translations-common -f %{_tmppath}/translations.common
%defattr(-,root,root)
%dir %{progdir}
%dir %{progdir}/chrome/

%files translations-other -f %{_tmppath}/translations.other
%defattr(-,root,root)
%dir %{progdir}
%dir %{progdir}/chrome/
%endif

%files branding-upstream  
%defattr(-,root,root)  
%dir %{progdir}
#%dir %{progdir}/defaults/
#%{progdir}/defaults/profile/bookmarks.html

%if %crashreporter && !0%{?use_xulrunner}
%files buildsymbols
%defattr(-,root,root)
%{_datadir}/mozilla/
%endif

%changelog
