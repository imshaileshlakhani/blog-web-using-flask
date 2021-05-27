-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 27, 2021 at 12:16 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `chatroom`
--

-- --------------------------------------------------------

--
-- Table structure for table `msg`
--

CREATE TABLE `msg` (
  `sno` int(11) NOT NULL,
  `msgs` text NOT NULL,
  `room` text NOT NULL,
  `ip` text NOT NULL,
  `stime` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `msg`
--

INSERT INTO `msg` (`sno`, `msgs`, `room`, `ip`, `stime`) VALUES
(11, 'Hi', 'shailesh', '::1', '2020-11-12 19:51:36'),
(12, 'Hi, How are you ?', 'shailesh', '::1', '2020-11-12 19:52:16'),
(13, 'I am Fine', 'shailesh', '::1', '2020-11-12 19:52:31'),
(14, 'what about you', 'shailesh', '::1', '2020-11-12 19:52:53'),
(15, 'hi', 'she', '::1', '2020-11-17 09:55:09'),
(16, 'how are you?', 'she', '::1', '2020-11-17 09:55:18'),
(17, 'hi', 'ravin12', '::1', '2020-11-17 19:37:32'),
(18, 'how are you?', 'ravin12', '::1', '2020-11-17 19:37:42'),
(19, 'hi', 'ankit', '::1', '2021-05-26 19:46:45'),
(20, 'hi', 'ankit', '::1', '2021-05-26 19:46:50'),
(21, 'how are you', 'ankit', '::1', '2021-05-26 19:46:59'),
(22, 'i am fine', 'ankit', '::1', '2021-05-26 19:47:07'),
(23, 'hi', 'sd', '::1', '2021-05-27 11:04:10'),
(24, 'how are you', 'sd', '::1', '2021-05-27 11:04:20'),
(25, 'hi', 'project', '::1', '2021-05-27 14:32:33'),
(26, 'how are you', 'project', '::1', '2021-05-27 14:32:44');

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `sno` int(11) NOT NULL,
  `roomname` text NOT NULL,
  `stime` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`sno`, `roomname`, `stime`) VALUES
(6, 'shailesh', '2020-11-12 19:50:56'),
(7, 'she', '2020-11-17 09:54:48'),
(8, 'ravin12', '2020-11-17 19:36:57'),
(9, 'ankit', '2021-05-26 19:45:51'),
(10, 'sd', '2021-05-27 11:03:44'),
(11, 'project', '2021-05-27 14:32:09');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `msg`
--
ALTER TABLE `msg`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `msg`
--
ALTER TABLE `msg`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `room`
--
ALTER TABLE `room`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
