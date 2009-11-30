#
# spec file for package MozillaFirefox (Version 3.6b4)
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2006-2009 Wolfgang Rosenauer
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
%define xulrunner mozilla-xulrunner192
BuildRequires:  autoconf213 gcc-c++ libgnomeui-devel libidl-devel libnotify-devel orbit-devel python unzip update-desktop-files zip
BuildRequires:  %{xulrunner}-devel = 1.9.2b4
%if %suse_version > 1020
BuildRequires:  fdupes
%endif
%if %suse_version > 1110
BuildRequires:  libiw-devel
%else
BuildRequires:  wireless-tools
%endif
License:        GPLv2+ ; LGPLv2.1+ ; MPLv1.1+
Provides:       web_browser
Provides:       firefox
Version:        3.6b4
Release:        1
%define         releasedate 2009112600
Summary:        Mozilla Firefox Web Browser
Url:            http://www.mozilla.org/
Group:          Productivity/Networking/Web/Browsers
Source:         firefox-%{version}-source.tar.bz2
Source1:        MozillaFirefox.desktop
Source2:        %{name}-rpmlintrc
Source3:        mozilla.sh.in
Source4:        find-external-requires.sh
# this needs to be shipped when lockdown changes are back
Source5:        firefox.schemas
Source6:        kde.js
Source7:        l10n-%{version}.tar.bz2
Source8:        firefox-mimeinfo.xml
Source16:       firefox.1
Source17:       firefox-suse-default-prefs.js
Patch1:         firefox-libxul-sdk.patch
Patch2:         firefox-credits.patch
Patch3:         toolkit-download-folder.patch
Patch4:         firefox-linkorder.patch
Patch5:         firefox-browser-css.patch
Patch6:         firefox-cross-desktop.patch
Patch7:         firefox-no-gnomevfs.patch
Patch8:         firefox-appname.patch
Patch9:         firefox-kde.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
PreReq:         coreutils /bin/sh shared-mime-info desktop-file-utils
Requires:       %{xulrunner} >= %(rpm -q --queryformat '%{VERSION}-%{RELEASE}' %{xulrunner})
%requires_eq    %{xulrunner}
%ifarch %ix86
Requires:       %{xulrunner}-32bit >= %(rpm -q --queryformat '%{VERSION}-%{RELEASE}' %{xulrunner})
Requires:       %{xulrunner}-32bit = %(rpm -q --queryformat '%{VERSION}' %{xulrunner})
%endif
Requires:       %{name}-branding >= 3.5
%define _use_internal_dependency_generator 0
%define __find_requires sh %{SOURCE4}
%global provfind sh -c "grep -v '.so' | %__find_provides"
%global __find_provides %provfind
%define progname firefox
%define progdir %{_prefix}/%_lib/%{progname}
%if %suse_version > 1020
%define gnome_dir     %{_prefix}
%else
%define gnome_dir     /opt/gnome
%endif
### build options
%define branding 1
%define localize 1 
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
PreReq:         %{name} = %{version}
Requires:       %{xulrunner}-translations-common
Obsoletes:      %{name}-translations < %{version}-%{release}

%description translations-common
This package contains several common languages for the user interface
of MozillaFirefox.

%package translations-other
Summary:        Extra translations for MozillaFirefox
License:        GPLv2+ ; LGPLv2.1+ ; MPLv1.1+
Provides:       locale(%{name}:be;bn_BD;cy;el;eo;et;eu;fa;fy_NL;ga_IE;gl;gu_IN;he;hi_IN;id;is;kk;kn;lt;lv;mk;ml;mr;nn_NO;or;pa_IN;rm;ro;si;sk;sl;sq;ta;ta_LK;te;tr;uk)
Group:          System/Localization
PreReq:         %{name} = %{version}
Requires:       %{xulrunner}-translations-other
Obsoletes:      %{name}-translations < %{version}-%{release}

%description translations-other
This package contains rarely used languages for the user interface
of MozillaFirefox.

%endif

%package branding-upstream
License:        GPLv2+ ; LGPLv2.1+ ; MPLv1.1+
Summary:        Upstream branding for MozillaFirefox
Group:          Productivity/Networking/Web/Browsers
Provides:       %{name}-branding = 3.5
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
%setup -q -n mozilla -b 7
cd $RPM_BUILD_DIR/mozilla
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%if %suse_version >= 1110
%patch9 -p1
# install kde.js
install -m 644 %{SOURCE6} browser/app/profile/kde.js
%endif

%build
export MOZ_BUILD_DATE=%{releasedate}
export MOZILLA_OFFICIAL=1
export BUILD_OFFICIAL=1
export CFLAGS="$RPM_OPT_FLAGS -Os -fno-strict-aliasing"  
export CXXFLAGS="$CFLAGS"
# 10.3-x86_64 build fails probably because gcc bug
%if %suse_version == 1030
%ifarch x86_64
export ac_cv_visibility_hidden="no"
%endif
%endif
export MOZCONFIG=$RPM_BUILD_DIR/mozconfig
SDKDIR=$(pkg-config --variable=sdkdir libxul)
cat << EOF > $MOZCONFIG
mk_add_options MOZILLA_OFFICIAL=1
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZ_MAKE_FLAGS=%{?jobs:-j%jobs}
. \$topsrcdir/browser/config/mozconfig
ac_add_options --prefix=%{_prefix}
ac_add_options --libdir=%{_libdir}
ac_add_options --sysconfdir=%{_sysconfdir}
ac_add_options --mandir=%{_mandir}
ac_add_options --includedir=%{_includedir}
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-libxul-sdk=$SDKDIR
ac_add_options --with-l10n-base=../l10n
ac_add_options --with-system-jpeg
#ac_add_options --with-system-png     # doesn't work because of missing APNG support
ac_add_options --with-system-zlib
ac_add_options --disable-installer
ac_add_options --disable-updater
ac_add_options --disable-tests
ac_add_options --disable-debug
ac_add_options --disable-crashreporter
EOF
%if %branding
cat << EOF >> $MOZCONFIG
ac_add_options --enable-official-branding
EOF
%endif
make -f client.mk build

%install
make -C browser/installer STRIP=/bin/true
# copy tree into RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{progdir}
cp -rf $RPM_BUILD_DIR/mozilla/dist/firefox/* $RPM_BUILD_ROOT/%{progdir}
# install additional locales
%if %localize
rm -f %{_tmppath}/translations.*
for locale in $(awk '{ print $1; }' browser/locales/shipped-locales); do
  case $locale in
   ja-JP-mac|en-US)
	;;
   *)
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
s:%%APPNAME:%{progname}:g
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
# apply SUSE defaults
sed -e 's,RPM_VERSION,%{version}-%{release},g' \
   %{SOURCE17} > suse-default-prefs
cp suse-default-prefs $RPM_BUILD_ROOT%{progdir}/defaults/preferences/firefox-build.js
rm suse-default-prefs
# use correct locale for useragent
cat > $RPM_BUILD_ROOT%{progdir}/defaults/preferences/firefox-l10n.js << EOF
pref("general.useragent.locale", "chrome://global/locale/intl.properties");
EOF
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
%if %suse_version > 1020
%fdupes $RPM_BUILD_ROOT%{progdir}
%fdupes $RPM_BUILD_ROOT%{_datadir}
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
# move plugins to new location
if [ "$1" = "2" ]; then
  if [ -d /opt/MozillaFirefox/%{_lib}/plugins ]; then
    rm -rf /opt/MozillaFirefox/%{_lib}/plugins/libnullplugin.so
    cp -fud /opt/MozillaFirefox/%{_lib}/plugins/* %{progdir}/plugins
    rm -rf /opt/MozillaFirefox/%{_lib}/plugins
  fi
fi
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

%files
%defattr(-,root,root)
%dir %{progdir}
%dir %{progdir}/chrome/
%{progdir}/chrome/browser.*
%{progdir}/chrome/classic.*
%{progdir}/chrome/en-US.*
%{progdir}/chrome/reporter.*
%{progdir}/chrome/icons
%{progdir}/components/
%exclude %{progdir}/defaults/profile/bookmarks.html
%{progdir}/defaults/
%{progdir}/extensions/
%{progdir}/icons/
%{progdir}/searchplugins/
%{progdir}/modules/
%attr(755,root,root) %{progdir}/%{progname}.sh
%{progdir}/%{progname}
%{progdir}/application.ini
%{progdir}/blocklist.xml
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

%files translations-other -f %{_tmppath}/translations.other
%defattr(-,root,root)
%endif

%files branding-upstream  
%defattr(-,root,root)  
%{progdir}/browserconfig.properties  
%{progdir}/defaults/profile/bookmarks.html

%changelog
