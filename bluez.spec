#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : bluez
Version  : 5.80
Release  : 61
URL      : https://mirrors.kernel.org/pub/linux/bluetooth/bluez-5.80.tar.gz
Source0  : https://mirrors.kernel.org/pub/linux/bluetooth/bluez-5.80.tar.gz
Summary  : Bluetooth protocol stack for Linux
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: bluez-bin = %{version}-%{release}
Requires: bluez-config = %{version}-%{release}
Requires: bluez-data = %{version}-%{release}
Requires: bluez-lib = %{version}-%{release}
Requires: bluez-libexec = %{version}-%{release}
Requires: bluez-license = %{version}-%{release}
Requires: bluez-man = %{version}-%{release}
Requires: bluez-services = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : file
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(ell)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(json-c)
BuildRequires : pkgconfig(libebook-1.2)
BuildRequires : pkgconfig(libedataserver-1.2)
BuildRequires : pkgconfig(libical)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(sbc)
BuildRequires : pkgconfig(speexdsp)
BuildRequires : pypi-docutils
BuildRequires : pypi-pygments
BuildRequires : readline-dev
BuildRequires : systemd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
BlueZ - Bluetooth protocol stack for Linux
******************************************

%package bin
Summary: bin components for the bluez package.
Group: Binaries
Requires: bluez-data = %{version}-%{release}
Requires: bluez-libexec = %{version}-%{release}
Requires: bluez-config = %{version}-%{release}
Requires: bluez-license = %{version}-%{release}
Requires: bluez-services = %{version}-%{release}

%description bin
bin components for the bluez package.


%package config
Summary: config components for the bluez package.
Group: Default

%description config
config components for the bluez package.


%package data
Summary: data components for the bluez package.
Group: Data

%description data
data components for the bluez package.


%package dev
Summary: dev components for the bluez package.
Group: Development
Requires: bluez-lib = %{version}-%{release}
Requires: bluez-bin = %{version}-%{release}
Requires: bluez-data = %{version}-%{release}
Provides: bluez-devel = %{version}-%{release}
Requires: bluez = %{version}-%{release}

%description dev
dev components for the bluez package.


%package extras
Summary: extras components for the bluez package.
Group: Default

%description extras
extras components for the bluez package.


%package lib
Summary: lib components for the bluez package.
Group: Libraries
Requires: bluez-data = %{version}-%{release}
Requires: bluez-libexec = %{version}-%{release}
Requires: bluez-license = %{version}-%{release}

%description lib
lib components for the bluez package.


%package libexec
Summary: libexec components for the bluez package.
Group: Default
Requires: bluez-config = %{version}-%{release}
Requires: bluez-license = %{version}-%{release}

%description libexec
libexec components for the bluez package.


%package license
Summary: license components for the bluez package.
Group: Default

%description license
license components for the bluez package.


%package man
Summary: man components for the bluez package.
Group: Default

%description man
man components for the bluez package.


%package services
Summary: services components for the bluez package.
Group: Systemd services
Requires: systemd

%description services
services components for the bluez package.


%prep
%setup -q -n bluez-5.80
cd %{_builddir}/bluez-5.80
pushd ..
cp -a bluez-5.80 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742398279
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --enable-library \
--enable-manpages \
--with-dbusconfdir=/usr/share \
--enable-experimental \
--enable-deprecated \
--enable-hid2hci \
--sysconfdir=/usr/share/defaults/bluez
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --enable-library \
--enable-manpages \
--with-dbusconfdir=/usr/share \
--enable-experimental \
--enable-deprecated \
--enable-hid2hci \
--sysconfdir=/usr/share/defaults/bluez
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1742398279
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bluez
cp %{_builddir}/bluez-%{version}/COPYING %{buildroot}/usr/share/package-licenses/bluez/a7a897a4bde987e597c04f16a9c28f6d3f57916d || :
cp %{_builddir}/bluez-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/bluez/32c7c5556c56cdbb2d507e27d28d081595a35a9b || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
## install_append content
ln -sv bluetooth.service %{buildroot}/usr/lib/systemd/system/dbus-org.bluez.service
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib/udev/hid2hci
/V3/usr/lib64/cups/backend/bluetooth
/usr/lib/udev/hid2hci
/usr/lib64/cups/backend/bluetooth

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/bluemoon
/V3/usr/bin/bluetoothctl
/V3/usr/bin/btattach
/V3/usr/bin/btmon
/V3/usr/bin/hex2hcd
/V3/usr/bin/isotest
/V3/usr/bin/l2ping
/V3/usr/bin/l2test
/V3/usr/bin/mpris-proxy
/V3/usr/bin/rctest
/usr/bin/bluemoon
/usr/bin/bluetoothctl
/usr/bin/btattach
/usr/bin/btmon
/usr/bin/hex2hcd
/usr/bin/isotest
/usr/bin/l2ping
/usr/bin/l2test
/usr/bin/mpris-proxy
/usr/bin/rctest

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/97-hid2hci.rules

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/services/org.bluez.obex.service
/usr/share/dbus-1/system-services/org.bluez.service
/usr/share/dbus-1/system.d/bluetooth.conf
/usr/share/dbus-1/system.d/obex.conf
/usr/share/defaults/bluez/bluetooth/input.conf
/usr/share/defaults/bluez/bluetooth/main.conf
/usr/share/defaults/bluez/bluetooth/network.conf
/usr/share/zsh/site-functions/_bluetoothctl

%files dev
%defattr(-,root,root,-)
/usr/include/bluetooth/bluetooth.h
/usr/include/bluetooth/bnep.h
/usr/include/bluetooth/cmtp.h
/usr/include/bluetooth/hci.h
/usr/include/bluetooth/hci_lib.h
/usr/include/bluetooth/hidp.h
/usr/include/bluetooth/l2cap.h
/usr/include/bluetooth/rfcomm.h
/usr/include/bluetooth/sco.h
/usr/include/bluetooth/sdp.h
/usr/include/bluetooth/sdp_lib.h
/usr/lib64/libbluetooth.so
/usr/lib64/pkgconfig/bluez.pc

%files extras
%defattr(-,root,root,-)
/V3/usr/bin/ciptool
/V3/usr/bin/hciattach
/V3/usr/bin/hciconfig
/V3/usr/bin/hcidump
/V3/usr/bin/hcitool
/V3/usr/bin/rfcomm
/V3/usr/bin/sdptool
/usr/bin/ciptool
/usr/bin/hciattach
/usr/bin/hciconfig
/usr/bin/hcidump
/usr/bin/hcitool
/usr/bin/rfcomm
/usr/bin/sdptool
/usr/share/man/man1/ciptool.1
/usr/share/man/man1/hciattach.1
/usr/share/man/man1/hciconfig.1
/usr/share/man/man1/hcidump.1
/usr/share/man/man1/hcitool.1
/usr/share/man/man1/rfcomm.1
/usr/share/man/man1/sdptool.1

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libbluetooth.so.3.19.15
/usr/lib64/libbluetooth.so.3
/usr/lib64/libbluetooth.so.3.19.15

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/bluetooth/bluetoothd
/V3/usr/libexec/bluetooth/obexd
/usr/libexec/bluetooth/bluetoothd
/usr/libexec/bluetooth/obexd

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bluez/32c7c5556c56cdbb2d507e27d28d081595a35a9b
/usr/share/package-licenses/bluez/a7a897a4bde987e597c04f16a9c28f6d3f57916d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/bluetoothctl-admin.1
/usr/share/man/man1/bluetoothctl-advertise.1
/usr/share/man/man1/bluetoothctl-assistant.1
/usr/share/man/man1/bluetoothctl-endpoint.1
/usr/share/man/man1/bluetoothctl-gatt.1
/usr/share/man/man1/bluetoothctl-hci.1
/usr/share/man/man1/bluetoothctl-mgmt.1
/usr/share/man/man1/bluetoothctl-monitor.1
/usr/share/man/man1/bluetoothctl-player.1
/usr/share/man/man1/bluetoothctl-scan.1
/usr/share/man/man1/bluetoothctl-transport.1
/usr/share/man/man1/bluetoothctl.1
/usr/share/man/man1/btattach.1
/usr/share/man/man1/btmgmt.1
/usr/share/man/man1/btmon.1
/usr/share/man/man1/hid2hci.1
/usr/share/man/man1/isotest.1
/usr/share/man/man1/l2ping.1
/usr/share/man/man1/rctest.1
/usr/share/man/man5/org.bluez.Adapter.5
/usr/share/man/man5/org.bluez.AdminPolicySet.5
/usr/share/man/man5/org.bluez.AdminPolicyStatus.5
/usr/share/man/man5/org.bluez.AdvertisementMonitor.5
/usr/share/man/man5/org.bluez.AdvertisementMonitorManager.5
/usr/share/man/man5/org.bluez.Agent.5
/usr/share/man/man5/org.bluez.AgentManager.5
/usr/share/man/man5/org.bluez.Battery.5
/usr/share/man/man5/org.bluez.BatteryProvider.5
/usr/share/man/man5/org.bluez.BatteryProviderManager.5
/usr/share/man/man5/org.bluez.Device.5
/usr/share/man/man5/org.bluez.DeviceSet.5
/usr/share/man/man5/org.bluez.GattCharacteristic.5
/usr/share/man/man5/org.bluez.GattDescriptor.5
/usr/share/man/man5/org.bluez.GattManager.5
/usr/share/man/man5/org.bluez.GattProfile.5
/usr/share/man/man5/org.bluez.GattService.5
/usr/share/man/man5/org.bluez.Input.5
/usr/share/man/man5/org.bluez.LEAdvertisement.5
/usr/share/man/man5/org.bluez.LEAdvertisingManager.5
/usr/share/man/man5/org.bluez.Media.5
/usr/share/man/man5/org.bluez.MediaAssistant.5
/usr/share/man/man5/org.bluez.MediaControl.5
/usr/share/man/man5/org.bluez.MediaEndpoint.5
/usr/share/man/man5/org.bluez.MediaFolder.5
/usr/share/man/man5/org.bluez.MediaItem.5
/usr/share/man/man5/org.bluez.MediaPlayer.5
/usr/share/man/man5/org.bluez.MediaTransport.5
/usr/share/man/man5/org.bluez.Network.5
/usr/share/man/man5/org.bluez.NetworkServer.5
/usr/share/man/man5/org.bluez.Profile.5
/usr/share/man/man5/org.bluez.ProfileManager.5
/usr/share/man/man5/org.bluez.obex.Agent.5
/usr/share/man/man5/org.bluez.obex.AgentManager.5
/usr/share/man/man5/org.bluez.obex.Client.5
/usr/share/man/man5/org.bluez.obex.FileTransfer.5
/usr/share/man/man5/org.bluez.obex.Image.5
/usr/share/man/man5/org.bluez.obex.Message.5
/usr/share/man/man5/org.bluez.obex.MessageAccess.5
/usr/share/man/man5/org.bluez.obex.ObjectPush.5
/usr/share/man/man5/org.bluez.obex.PhonebookAccess.5
/usr/share/man/man5/org.bluez.obex.Session.5
/usr/share/man/man5/org.bluez.obex.Synchronization.5
/usr/share/man/man5/org.bluez.obex.Transfer.5
/usr/share/man/man7/hci.7
/usr/share/man/man7/l2cap.7
/usr/share/man/man7/rfcomm.7
/usr/share/man/man8/bluetoothd.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/bluetooth.service
/usr/lib/systemd/system/dbus-org.bluez.service
/usr/lib/systemd/user/dbus-org.bluez.obex.service
/usr/lib/systemd/user/mpris-proxy.service
/usr/lib/systemd/user/obex.service
