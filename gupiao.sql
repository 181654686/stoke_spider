/*
 Navicat MySQL Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 50733
 Source Host           : localhost:3306
 Source Schema         : gupiao

 Target Server Type    : MySQL
 Target Server Version : 50733
 File Encoding         : 65001

 Date: 27/04/2021 09:02:31
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for main_list
-- ----------------------------
DROP TABLE IF EXISTS `main_list`;
CREATE TABLE `main_list`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stock_abbr` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `stock_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `stock_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `stock_number` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `stock_pinyin` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `dt` datetime NULL DEFAULT NULL,
  `done` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6813 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for stoke_caiwu_history
-- ----------------------------
DROP TABLE IF EXISTS `stoke_caiwu_history`;
CREATE TABLE `stoke_caiwu_history`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `value` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `stokeid` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `caiwutype` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 29593 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for stoke_cashflow_history
-- ----------------------------
DROP TABLE IF EXISTS `stoke_cashflow_history`;
CREATE TABLE `stoke_cashflow_history`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `value` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `stokeid` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 933 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for stoke_debtratio_history
-- ----------------------------
DROP TABLE IF EXISTS `stoke_debtratio_history`;
CREATE TABLE `stoke_debtratio_history`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `value` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `stokeid` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 943 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for stoke_grossprofit_history
-- ----------------------------
DROP TABLE IF EXISTS `stoke_grossprofit_history`;
CREATE TABLE `stoke_grossprofit_history`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `value` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `stokeid` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1111 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for stoke_guxi_history
-- ----------------------------
DROP TABLE IF EXISTS `stoke_guxi_history`;
CREATE TABLE `stoke_guxi_history`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL,
  `value` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `stokeid` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 176084 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for stoke_income_history
-- ----------------------------
DROP TABLE IF EXISTS `stoke_income_history`;
CREATE TABLE `stoke_income_history`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `value` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `stokeid` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1111 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for stoke_pb_history
-- ----------------------------
DROP TABLE IF EXISTS `stoke_pb_history`;
CREATE TABLE `stoke_pb_history`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL,
  `value` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `stokeid` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 224820 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for stoke_pea_history
-- ----------------------------
DROP TABLE IF EXISTS `stoke_pea_history`;
CREATE TABLE `stoke_pea_history`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL,
  `value` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `stokeid` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 231914 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for stoke_price_history
-- ----------------------------
DROP TABLE IF EXISTS `stoke_price_history`;
CREATE TABLE `stoke_price_history`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL,
  `value` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `stokeid` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 262709 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for stoke_profit_history
-- ----------------------------
DROP TABLE IF EXISTS `stoke_profit_history`;
CREATE TABLE `stoke_profit_history`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `value` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `stokeid` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1106 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for stoke_profit_kf_history
-- ----------------------------
DROP TABLE IF EXISTS `stoke_profit_kf_history`;
CREATE TABLE `stoke_profit_kf_history`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `value` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `stokeid` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 966 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for stoke_roa_history
-- ----------------------------
DROP TABLE IF EXISTS `stoke_roa_history`;
CREATE TABLE `stoke_roa_history`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `value` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `stokeid` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 971 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for stoke_roe_history
-- ----------------------------
DROP TABLE IF EXISTS `stoke_roe_history`;
CREATE TABLE `stoke_roe_history`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `value` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `stokeid` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 22 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for stoke_value_history
-- ----------------------------
DROP TABLE IF EXISTS `stoke_value_history`;
CREATE TABLE `stoke_value_history`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL,
  `value` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `stokeid` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 231982 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
