Name:           ros-kinetic-rqt-bag
Version:        0.4.10
Release:        0%{?dist}
Summary:        ROS rqt_bag package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/rqt_bag
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python-rospkg
Requires:       ros-kinetic-python-qt-binding >= 0.2.19
Requires:       ros-kinetic-rosbag
Requires:       ros-kinetic-rosgraph-msgs
Requires:       ros-kinetic-roslib
Requires:       ros-kinetic-rosnode
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-rqt-gui >= 0.2.12
Requires:       ros-kinetic-rqt-gui-py
BuildRequires:  ros-kinetic-catkin

%description
rqt_bag provides a GUI plugin for displaying and replaying ROS bag files.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Oct 25 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.4.10-0
- Autogenerated by Bloom

* Fri Oct 13 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.4.9-0
- Autogenerated by Bloom

* Fri Apr 28 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.4.8-0
- Autogenerated by Bloom

