#
# spec file for package mozilla-xulrunner192 (Version 1.9.2.2)
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


Name:           mozilla-xulrunner192
BuildRequires:  autoconf213 gcc-c++ libcurl-devel libgnomeui-devel libidl-devel libnotify-devel python startup-notification-devel zip
# needed for brp-check-bytecode-version (jar, fastjar would do as well)
BuildRequires:  unzip
%if %suse_version > 1020
BuildRequires:  fdupes
%endif
%if %suse_version > 1030
BuildRequires:  hunspell-devel
%endif
%if %suse_version > 1100
BuildRequires:  nss-shared-helper-devel
%endif
%if %suse_version > 1110
BuildRequires:  libiw-devel
BuildRequires:  libproxy-devel
%else
BuildRequires:  wireless-tools
%endif
License:        GPLv2+ ; LGPLv2.1+ ; MPLv1.1+
Version:        1.9.2.2
Release:        1
%define         releasedate 2010031700
%define         version_internal 1.9.2.2
%define         apiversion 1.9.2
%define         uaweight 192020
Summary:        Mozilla Runtime Environment 1.9.2
Url:            http://www.mozilla.org
Group:          Productivity/Other
Provides:       gecko192
%if %suse_version >= 1110
# this is needed to match this package with the kde4 helper package without the main package
# having a hard requirement on the kde4 package
%define kde_helper_version 6
Provides:       mozilla-kde4-version = %{kde_helper_version}
%endif
%ifarch %ix86
Provides:       mozilla-xulrunner192-32bit = %{version}-%{release}
%endif
Source:         xulrunner-source-%{version}.tar.bz2
Source1:        l10n-%{version}.tar.bz2
Source2:        find-external-requires.sh
Source3:        %{name}-rpmlintrc
Source4:        xulrunner-openSUSE-prefs.js
Source5:        add-plugins.sh.in
Source6:        create-tar.sh
Source7:        baselibs.conf
Source8:        toolkit-lockdown.js
Patch1:         toolkit-download-folder.patch
Patch2:         mozilla-libproxy.patch
Patch3:         mozilla-pkgconfig.patch
Patch4:         idldir.patch
Patch5:         mozilla-nongnome-proxies.patch
Patch6:         mozilla-helper-app.patch
Patch7:         mozilla-prefer_plugin_pref.patch
Patch8:         mozilla-shared-nss-db.patch
Patch9:         mozilla-startup-notification.patch
Patch10:        mozilla-kde.patch
# PATCH-FEATURE-SLED FATE#302023, FATE#302024
Patch11:        mozilla-gconf-backend.patch
Patch12:        gecko-lockdown.patch
Patch13:        toolkit-ui-lockdown.patch
# ---
Patch14:        mozilla-breakpad-update.patch
Patch15:        mozilla-ua-locale-pref.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires(post):  update-alternatives coreutils
Requires(preun): update-alternatives coreutils
### build configuration ###
%ifarch %ix86
%define crashreporter    1
%else
%define crashreporter    0
%endif
%define has_system_nspr  0
%define has_system_nss   0
%define has_system_cairo 0
%define localize 1
%if %suse_version > 1030 || 0%{?opensuse_bs}
%define has_system_nspr  1
%define has_system_nss   1
%endif
%if %suse_version > 1110
%define has_system_cairo 1
%endif
### configuration end ###
%define _use_internal_dependency_generator 0
%define __find_requires sh %{SOURCE2}
%global provfind sh -c "grep -v 'libsqlite3.so' | %__find_provides"
%global __find_provides %provfind
%if %has_system_nspr
BuildRequires:  mozilla-nspr-devel
Requires:       mozilla-nspr >= %(rpm -q --queryformat '%{VERSION}' mozilla-nspr)
%endif
%if %has_system_nss
BuildRequires:  mozilla-nss-devel >= 3.12.6
Requires:       mozilla-nss >= %(rpm -q --queryformat '%{VERSION}' mozilla-nss)
%endif
Recommends:     %{name}-gnome

%description
XULRunner is a single installable package that can be used to bootstrap
multiple XUL+XPCOM applications that are as rich as Firefox and
Thunderbird.


%package devel
License:        GPLv2+ ; LGPLv2.1+ ; MPLv1.1+
Summary:        XULRunner/Gecko SDK 1.9.2
Group:          Development/Libraries/Other
%if %has_system_nspr
Requires:       mozilla-nspr-devel >= %(rpm -q --queryformat '%{VERSION}' mozilla-nspr-devel) 
%endif
%if %has_system_nss
Requires:       mozilla-nss-devel >= %(rpm -q --queryformat '%{VERSION}' mozilla-nss-devel)
%endif
Requires:       %{name} = %{version}

%description devel
Software Development Kit to embed XUL or Gecko into other applications.

%if %localize
%package translations-common
License:        GPLv2+ ; LGPLv2.1+ ; MPLv1.1+
Summary:        Common translations for XULRunner 1.9.2
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:ar;ca;cs;da;de;en_GB;es_AR;es_CL;es_ES;fi;fr;hu;it;ja;ko;nb_NO;nl;pl;pt_BR;pt_PT;ru;sv_SE;zh_CN;zh_TW)
Obsoletes:      %{name}-translations < %{version}-%{release}

%description translations-common
XULRunner is a single installable package that can be used to bootstrap
multiple XUL+XPCOM applications that are as rich as Firefox and
Thunderbird.

This package contains the most common languages but en-US which is
delivered in the main package.


%package translations-other
License:        GPLv2+ ; LGPLv2.1+ ; MPLv1.1+
Summary:        Extra translations for XULRunner 1.9.2
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:af;as;be;bg;bn_BD;bn_IN;cy;el;eo;es_MX;et;eu;fa;fy_NL;ga_IE;gl;gu_IN;he;hi_IN;hr;id;is;ka;kk;kn;ku;lt;lv;mk;ml;mr;nn_NO;oc;or;pa_IN;rm;ro;si;sk;sl;sq;sr;ta;ta_LK;te;th;tr;uk;vi)
Obsoletes:      %{name}-translations < %{version}-%{release}

%description translations-other
XULRunner is a single installable package that can be used to bootstrap
multiple XUL+XPCOM applications that are as rich as Firefox and
Thunderbird.

This package contains rarely used languages.
%endif

%package gnome
License:        GPLv2+ ; LGPLv2.1+ ; MPLv1.1+
Summary:        XULRunner components depending on gnome-vfs
Group:          Productivity/Other
Requires:       %{name} = %{version}-%{release}
Requires(post): coreutils

%description gnome
This subpackage contains the Necko Gnome-VFS and Gnome components which
rely on the gnome-vfs subsystem to be installed. They are recommended
for full desktop integration but not mandatory for small disk footprint
KDE installations for example.


%if %crashreporter
%package buildsymbols
License:        GPLv2+ ; LGPLv2.1+ ; MPLv1.1+
Summary:        Breakpad buildsymbols for %{name}
Group:          Development/Debug

%description buildsymbols
This subpackage contains the Breakpad created and compatible debugging
symbols meant for upload to Mozilla's crash collector database.
%endif


%prep
%setup -n mozilla -q -b 1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%if %suse_version >= 1110
%patch10 -p1
%endif
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
# bmo#542999
%patch15 -p1

%build
%if %suse_version >= 1110
kdehelperversion=$(cat toolkit/xre/nsKDEUtils.cpp | grep '#define KMOZILLAHELPER_VERSION' | cut -d ' ' -f 3)
if test "$kdehelperversion" != %{kde_helper_version}; then
  echo fix kde helper version in the .spec file
  exit 1
fi
%endif
MOZ_APP_DIR=%{_libdir}/xulrunner-%{version_internal}
export MOZ_BUILD_DATE=%{releasedate}
export CFLAGS="$RPM_OPT_FLAGS -Os -fno-strict-aliasing"
%if %crashreporter
export CFLAGS="$CFLAGS -gstabs+"
%endif
%ifarch ppc64
export CFLAGS="$CFLAGS -mminimal-toc"
%endif
# 10.3-x86_64 build fails probably because gcc bug
%if %suse_version == 1030
%ifarch x86_64
export ac_cv_visibility_hidden="no"
%endif
%endif
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-Wl,-rpath -Wl,${MOZ_APP_DIR}"
export MOZCONFIG=$RPM_BUILD_DIR/mozconfig
export MOZILLA_OFFICIAL=1
export BUILD_OFFICIAL=1
export MOZ_MILESTONE_RELEASE=1
#
cat << EOF > $MOZCONFIG
mk_add_options MOZILLA_OFFICIAL=1
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZ_MILESTONE_RELEASE=1
mk_add_options MOZ_MAKE_FLAGS=%{?jobs:-j%jobs}
mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/../obj
. \$topsrcdir/xulrunner/config/mozconfig
ac_add_options --prefix=%{_prefix}
ac_add_options --libdir=%{_libdir}
ac_add_options --sysconfdir=%{_sysconfdir}
ac_add_options --mandir=%{_mandir}
ac_add_options --includedir=%{_includedir}
ac_add_options --enable-optimize
ac_add_options --enable-extensions=default
ac_add_options --with-system-jpeg
#ac_add_options --with-system-png # no APNG support
ac_add_options --with-system-zlib
ac_add_options --with-l10n-base=../l10n
ac_add_options --enable-xft
ac_add_options --disable-freetype2
ac_add_options --enable-svg
ac_add_options --enable-canvas
ac_add_options --disable-tests
ac_add_options --disable-mochitest
ac_add_options --disable-installer
ac_add_options --disable-updater
ac_add_options --disable-javaxpcom
ac_add_options --enable-startup-notification
ac_add_options --enable-url-classifier
#ac_add_options --enable-debug
EOF
%if %has_system_nspr
cat << EOF >> $MOZCONFIG
ac_add_options --with-system-nspr
EOF
%endif
%if %has_system_nss
cat << EOF >> $MOZCONFIG
ac_add_options --with-system-nss
EOF
%endif
%if %has_system_cairo
cat << EOF >> $MOZCONFIG
ac_add_options --enable-system-cairo
EOF
%endif
%if %suse_version > 1030
cat << EOF >> $MOZCONFIG
ac_add_options --enable-system-hunspell
EOF
%endif
#%if %suse_version > 1100
#cat << EOF >> $MOZCONFIG
#ac_add_options --enable-system-sqlite
#EOF
#%endif
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
cd ../obj
%makeinstall STRIP=/bin/true
# remove some executable permissions
find $RPM_BUILD_ROOT%{_includedir}/xulrunner-%{version_internal} \
     -type f -perm -111 -exec chmod a-x {} \;
find $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/ \
     -name "*.js" -o -name "*.xpm" -o -name "*.png" | xargs chmod a-x
mkdir -p $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/extensions
# fixing SDK dynamic libs (symlink instead of copy)
rm $RPM_BUILD_ROOT%{_libdir}/xulrunner-devel-%{version_internal}/sdk/lib/*.so
ln -sf ../../../xulrunner-%{version_internal}/libmozjs.so \
       $RPM_BUILD_ROOT%{_libdir}/xulrunner-devel-%{version_internal}/sdk/lib/
ln -sf ../../../xulrunner-%{version_internal}/libxpcom.so \
       $RPM_BUILD_ROOT%{_libdir}/xulrunner-devel-%{version_internal}/sdk/lib/
ln -sf ../../../xulrunner-%{version_internal}/libxul.so \
       $RPM_BUILD_ROOT%{_libdir}/xulrunner-devel-%{version_internal}/sdk/lib/
# include basic buildenv for xulapps to use
mkdir -p $RPM_BUILD_ROOT%{_datadir}/xulrunner-%{version_internal}
pushd ..
# this list has been compiled by trial and error for prism
tar --exclude=*.cpp --exclude=*.mm \
   -cvjf $RPM_BUILD_ROOT%{_datadir}/xulrunner-%{version_internal}/mozilla-src.tar.bz2 \
    mozilla/configure.in mozilla/Makefile.in mozilla/client.py mozilla/allmakefiles.sh \
    mozilla/config mozilla/client.mk mozilla/aclocal.m4 mozilla/build mozilla/js/src/* \
    mozilla/testing mozilla/toolkit/mozapps/installer mozilla/probes mozilla/memory \
    mozilla/toolkit/xre mozilla/nsprpub/config mozilla/tools mozilla/xpcom/build
popd
# XPI example
#cp -rL dist/xpi-stage/simple $RPM_BUILD_ROOT/%{_libdir}/xulrunner-%{version_internal}/
# preferences
cp %{SOURCE4} $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/greprefs/all-openSUSE.js
cp %{SOURCE8} $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/greprefs/lockdown.js
# install add-plugins.sh
sed "s:%%PROGDIR:%{_libdir}/xulrunner-%{version_internal}:g" \
  %{SOURCE5} > $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/add-plugins.sh
chmod 755 $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/add-plugins.sh
# 64bit classification for GRE config
%ifarch x86_64 s390x ppc64
mv $RPM_BUILD_ROOT%{_sysconfdir}/gre.d/%{version_internal}.system.conf \
   $RPM_BUILD_ROOT%{_sysconfdir}/gre.d/%{version_internal}-64bit.system.conf
%endif
# ghosts
touch $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/global.reginfo
# install additional locales
%if %localize
rm -f %{_tmppath}/translations.*
for locale in $(awk '{ print $1; }' ../mozilla/browser/locales/shipped-locales); do
  case $locale in
   ja-JP-mac|en-US)
      ;;
   *)
      make -C toolkit/locales libs-$locale
      cp dist/xpi-stage/locale-$locale/chrome/$locale.jar \
         $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/chrome
      cp dist/xpi-stage/locale-$locale/chrome/$locale.manifest \
         $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/chrome
      # check against the fixed common list and sort into the right filelist
      _matched=0
      for _match in ar ca cs da de en-GB es-AR es-CL es-ES fi fr hu it ja ko nb-NO nl pl pt-BR pt-PT ru sv-SE zh-CN zh-TW; do
        [ "$_match" = "$locale" ] && _matched=1
      done
      [ $_matched -eq 1 ] && _l10ntarget=common || _l10ntarget=other
      echo %{_libdir}/xulrunner-%{version_internal}/chrome/$locale.jar \
         >> %{_tmppath}/translations.$_l10ntarget
      echo %{_libdir}/xulrunner-%{version_internal}/chrome/$locale.manifest \
         >> %{_tmppath}/translations.$_l10ntarget
  esac
done
%endif
# API symlink
ln -sf xulrunner-%{version_internal} $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{apiversion}
# compat links
%if 0%{?ga_version:1}
touch $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{ga_version}
%endif
# excludes
%if %suse_version < 1120
rm -f $RPM_BUILD_ROOT%{_bindir}/xulrunner
%endif
rm -f $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/updater
rm -f $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/update.locale
rm -f $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/LICENSE
rm -f $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/README.txt
rm -f $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/dictionaries/en-US*
# autoreg
touch $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/.autoreg
# fdupes
%if %suse_version > 1020
%fdupes $RPM_BUILD_ROOT%{_includedir}/xulrunner-%{version_internal}/
%fdupes $RPM_BUILD_ROOT%{_libdir}/xulrunner-%{version_internal}/
%endif
# create breakpad debugsymbols
%if %crashreporter
SYMBOLS_NAME="xulrunner-%{version}-%{release}.%{_arch}-%{suse_version}-symbols"
make buildsymbols \
  SYMBOL_INDEX_NAME="$SYMBOLS_NAME.txt" \
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
/usr/sbin/update-alternatives --install %{_bindir}/xulrunner \
  xulrunner %{_libdir}/xulrunner-%{version_internal}/xulrunner %{uaweight} || :
%{_libdir}/xulrunner-%{version_internal}/add-plugins.sh > /dev/null 2>&1
exit 0

%posttrans
# needed for updates which transition directory to symlink
%if 0%{?ga_version:1} 
test -d %{_libdir}/xulrunner-%{ga_version} && rm -rf %{_libdir}/xulrunner-%{ga_version}
ln -sf xulrunner-%{version_internal} %{_libdir}/xulrunner-%{ga_version}
%endif
[ -e %{_libdir}/xulrunner-%{version_internal}/add-plugins.sh ] && \
  %{_libdir}/xulrunner-%{version_internal}/add-plugins.sh > /dev/null 2>&1
exit 0

%preun
if [ "$1" = "0" ]; then # deinstallation
  # that's not quite nice since old versions should be removed on update as well
  # but that's problematic for updates w/o raising the version number
  /usr/sbin/update-alternatives --remove xulrunner %{_libdir}/xulrunner-%{version_internal}/xulrunner
fi
rm -f %{_libdir}/xulrunner-%{version_internal}/dictionaries/*
exit 0

%triggerin -- myspell-dictionary
%{_libdir}/xulrunner-%{version_internal}/add-plugins.sh > /dev/null 2>&1
exit 0

%triggerpostun -- myspell-dictionary
%{_libdir}/xulrunner-%{version_internal}/add-plugins.sh > /dev/null 2>&1
exit 0

%post gnome
touch %{_libdir}/xulrunner-%{version_internal}/.autoreg
exit 0

%files
%defattr(-,root,root)
%dir %{_libdir}/xulrunner-%{version_internal}/
%dir %{_libdir}/xulrunner-%{version_internal}/chrome/
%dir %{_libdir}/xulrunner-%{version_internal}/dictionaries/
%dir %{_libdir}/xulrunner-%{version_internal}/extensions/
%{_libdir}/xulrunner-%{version_internal}/chrome/classic.*
%{_libdir}/xulrunner-%{version_internal}/chrome/comm.*
%{_libdir}/xulrunner-%{version_internal}/chrome/en-US.*
%{_libdir}/xulrunner-%{version_internal}/chrome/pippki.*
%{_libdir}/xulrunner-%{version_internal}/chrome/toolkit.*
%{_libdir}/xulrunner-%{version_internal}/chrome/icons/
%{_libdir}/xulrunner-%{version_internal}/components/
%exclude %{_libdir}/xulrunner-%{version_internal}/components/libmozgnome.so
%exclude %{_libdir}/xulrunner-%{version_internal}/components/libnkgnomevfs.so
%{_libdir}/xulrunner-%{version_internal}/defaults/
%dir %{_libdir}/xulrunner-%{version_internal}/greprefs/
%{_libdir}/xulrunner-%{version_internal}/greprefs/all.js
%{_libdir}/xulrunner-%{version_internal}/greprefs/security-prefs.js
%{_libdir}/xulrunner-%{version_internal}/greprefs/xpinstall.js
%{_libdir}/xulrunner-%{version_internal}/greprefs/all-openSUSE.js
%{_libdir}/xulrunner-%{version_internal}/greprefs/lockdown.js
%{_libdir}/xulrunner-%{version_internal}/icons/
%{_libdir}/xulrunner-%{version_internal}/modules/
%{_libdir}/xulrunner-%{version_internal}/plugins/
%{_libdir}/xulrunner-%{version_internal}/res/
%{_libdir}/xulrunner-%{version_internal}/*.so
%{_libdir}/xulrunner-%{version_internal}/.autoreg
%{_libdir}/xulrunner-%{version_internal}/add-plugins.sh
%{_libdir}/xulrunner-%{version_internal}/dependentlibs.list
%{_libdir}/xulrunner-%{version_internal}/mozilla-xremote-client
%{_libdir}/xulrunner-%{version_internal}/run-mozilla.sh
%{_libdir}/xulrunner-%{version_internal}/xulrunner
%{_libdir}/xulrunner-%{version_internal}/xulrunner-bin
%{_libdir}/xulrunner-%{version_internal}/xulrunner-stub
%{_libdir}/xulrunner-%{version_internal}/platform.ini
# crashreporter files
%if %crashreporter
%{_libdir}/xulrunner-%{version_internal}/crashreporter
%{_libdir}/xulrunner-%{version_internal}/crashreporter.ini
%{_libdir}/xulrunner-%{version_internal}/Throbber-small.gif
%endif
# ghosts
%ghost %{_libdir}/xulrunner-%{version_internal}/global.reginfo
%if %suse_version >= 1120
%ghost %{_bindir}/xulrunner
%endif
# GRE
%dir %{_sysconfdir}/gre.d/
%attr(644,root,root) %{_sysconfdir}/gre.d/*
# API symlink
%{_libdir}/xulrunner-%{apiversion}
# compat symlinks
%if 0%{?ga_version:1} 
%ghost %{_libdir}/xulrunner-%{ga_version}
%endif

%files devel
%defattr(-,root,root)
%{_libdir}/xulrunner-%{version_internal}/xpcshell
%{_libdir}/xulrunner-%{version_internal}/xpidl
%{_libdir}/xulrunner-%{version_internal}/xpt_dump
%{_libdir}/xulrunner-%{version_internal}/xpt_link
%{_libdir}/xulrunner-devel-%{version_internal}/
# FIXME symlink dynamic libs below sdk/lib
%attr(644,root,root) %{_libdir}/pkgconfig/*
%{_includedir}/xulrunner-%{version_internal}/
%{_datadir}/xulrunner-%{version_internal}/

%files gnome
%defattr(-,root,root)
%dir %{_libdir}/xulrunner-%{version_internal}/
%dir %{_libdir}/xulrunner-%{version_internal}/components/
%ghost %{_libdir}/xulrunner-%{version_internal}/.autoreg
%{_libdir}/xulrunner-%{version_internal}/components/libmozgnome.so
%{_libdir}/xulrunner-%{version_internal}/components/libnkgnomevfs.so

%if %localize
%files translations-common -f %{_tmppath}/translations.common
%defattr(-,root,root)
%dir %{_libdir}/xulrunner-%{version_internal}/
%dir %{_libdir}/xulrunner-%{version_internal}/chrome/

%files translations-other -f %{_tmppath}/translations.other
%defattr(-,root,root)
%dir %{_libdir}/xulrunner-%{version_internal}/
%dir %{_libdir}/xulrunner-%{version_internal}/chrome/
%endif

%if %crashreporter
%files buildsymbols
%defattr(-,root,root)
%{_datadir}/mozilla/
%endif

%changelog
