#
# spec file for package MozillaFirefox (Version 4.0b9)
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#               2006-2011 Wolfgang Rosenauer
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
%define use_xulrunner 1
%define xulrunner mozilla-xulrunner20
BuildRequires:  autoconf213 gcc-c++ libcurl-devel libgnomeui-devel libidl-devel libnotify-devel python unzip update-desktop-files zip fdupes Mesa-devel yasm
%if %suse_version > 1110
BuildRequires:  libiw-devel
%else
BuildRequires:  wireless-tools
%endif
%if 0%{?use_xulrunner}
BuildRequires:  %{xulrunner}-devel = 2.0b9
%endif
License:        GPLv2+ ; LGPLv2.1+ ; MPLv1.1+
Version:        4.0b9
Provides:       web_browser
Provides:       firefox = %{version}
Release:        1
%define         releasedate 2011011000
Summary:        Mozilla Firefox Web Browser
Url:            http://www.mozilla.org/
Group:          Productivity/Networking/Web/Browsers
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
Source11:       firefox.1
Patch1:         toolkit-download-folder.patch
Patch2:         firefox-linkorder.patch
Patch3:         firefox-browser-css.patch
Patch4:         firefox-cross-desktop.patch
Patch5:         firefox-kde.patch
Patch6:         firefox-ui-lockdown.patch
Patch7:         firefox-no-sync-l10n.patch
Patch8:         firefox-libxulsdk-locales.patch
Patch9:        firefox-no-default-ualocale.patch
Patch10:        firefox-multilocale-chrome.patch
Patch11:        firefox-shell-bmo624267.patch
Patch12:        firefox-shellservice.patch
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
%if %suse_version > 1130
%define desktop_file_name firefox
%else
%define desktop_file_name %{name}
%endif
### build options
%define branding 1
%define localize 1
%ifarch ppc ppc64 s390 s390x ia64
%define crashreporter    0
%else
%define crashreporter    1
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


%prep
%setup -q -n mozilla -b 7 -b 10
cd $RPM_BUILD_DIR/mozilla
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%if %suse_version >= 1110
%patch5 -p1
# install kde.js
install -m 644 %{SOURCE6} browser/app/profile/kde.js
%endif
#%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

%build
export MOZ_BUILD_DATE=%{releasedate}
export MOZILLA_OFFICIAL=1
export BUILD_OFFICIAL=1
export CFLAGS="$RPM_OPT_FLAGS -Os -fno-strict-aliasing"
export CXXFLAGS="$CFLAGS"
export MOZCONFIG=$RPM_BUILD_DIR/mozconfig
SDKDIR=$(pkg-config --variable=sdkdir libxul)
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
ac_add_options --with-system-jpeg
#ac_add_options --with-system-png     # doesn't work because of missing APNG support
ac_add_options --with-system-zlib
ac_add_options --disable-installer
ac_add_options --disable-updater
ac_add_options --disable-tests
ac_add_options --disable-debug
ac_add_options --enable-update-channel=beta
EOF
%if 0%{?use_xulrunner}
cat << EOF >> $MOZCONFIG
ac_add_options --with-libxul-sdk=$SDKDIR
ac_add_options --enable-chrome-format=jar
EOF
%endif
%if %branding
cat << EOF >> $MOZCONFIG
ac_add_options --enable-official-branding
EOF
%endif
%ifarch ppc ppc64 s390 s390x
cat << EOF >> $MOZCONFIG
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
mkdir -p $RPM_BUILD_ROOT%{progdir}/searchplugins
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
	cp -r dist/xpi-stage/locale-$locale \
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
%if %suse_version < 1140
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
%suse_update_desktop_file %{desktop_file_name} Network WebBrowser X-Ximian-Main X-Ximian-Toplevel GTK
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
if [ -f usr/bin/update-desktop-database ] ; then
  usr/bin/update-desktop-database > /dev/null || :
fi
exit 0

%postun
if [ -f usr/bin/update-mime-database ] ; then
  usr/bin/update-mime-database %{_datadir}/mime > /dev/null || :
fi
if [ -f usr/bin/update-desktop-database ] ; then
  usr/bin/update-desktop-database > /dev/null || :
fi

%files
%defattr(-,root,root)
%dir %{progdir}
%dir %{progdir}/chrome/
%{progdir}/chrome/browser.*
%{progdir}/chrome/localized.manifest
%{progdir}/chrome/nonlocalized.manifest
%{progdir}/chrome/en-US.*
%{progdir}/chrome/icons
%{progdir}/components/
%exclude %{progdir}/defaults/profile/bookmarks.html
%{progdir}/defaults/
%dir %{progdir}/extensions/
%{progdir}/extensions/testpilot@labs.mozilla.com
%{progdir}/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}
%{progdir}/icons/
%{progdir}/modules/
%{progdir}/searchplugins/
%attr(755,root,root) %{progdir}/%{progname}.sh
%{progdir}/firefox
%{progdir}/application.ini
%{progdir}/blocklist.xml
%if %crashreporter
%{progdir}/crashreporter-override.ini
%endif
%{progdir}/chrome.manifest
%{_datadir}/applications/%{desktop_file_name}.desktop
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
%dir %{progdir}/extensions/

%files translations-other -f %{_tmppath}/translations.other
%defattr(-,root,root)
%dir %{progdir}
%dir %{progdir}/extensions/
%endif

%files branding-upstream
%defattr(-,root,root)
%dir %{progdir}
%dir %{progdir}/defaults/
%{progdir}/defaults/profile/bookmarks.html

%changelog
