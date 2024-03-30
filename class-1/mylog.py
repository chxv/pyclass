import logging
import logging.handlers
import os

log_file_name = '../log/my.log'


# 日志打印的过滤器，用于修改被打印的日志内容
class ModifyFilename(logging.Filter):
    def filter(self, record):
        # 向上多取一级文件夹名，因为完整绝对路径太冗余，而只有文件名称不清晰
        dirname = os.path.basename(os.path.dirname(record.pathname))
        record.filename = os.path.join(dirname, record.filename)
        return True


# 初始化日志
def init_logger() -> logging.Logger:
    if not os.path.exists(os.path.dirname(log_file_name)):
        os.makedirs(os.path.dirname(log_file_name)) # 如果日志文件夹不存在，则创建
    t = logging.getLogger(__name__)  # 创建一个新的日志对象
    t.setLevel(logging.DEBUG)  # 设置最低打印级别，小于等于此级别的日志不会被打印

    # 每天打印到不同的日志文件里 'd'=天, 'h'=小时, 'm'=分钟
    rht = logging.handlers.TimedRotatingFileHandler(log_file_name, 'd')
    fmt = logging.Formatter("%(asctime)s %(levelname)s %(filename)s:%(lineno)s %(funcName)s - %(message)s",
                            "%Y-%m-%d %H:%M:%S")
    rht.setFormatter(fmt)
    t.addHandler(rht)
    t.addFilter(ModifyFilename())
    return t


# 这里把变量转化为可读的文本，在必要时输出到日志里
def textualize(var):
    msg = f'type: {type(var)}'
    if hasattr(var, '__str__'):  # 这个变量内部支持文本化，可以直接输出其内容
        msg += f', value: {str(var)}'
        return msg
    # 对于其他类型，检测其属性并输出
    if hasattr(var, '__len__'):
        msg += f', len: {len(var)}'
    if hasattr(var, '__getitem__'):
        msg += f', can get item'
    if hasattr(var, '__iter__'):
        msg += f', is iterable'
    if hasattr(var, '__call__'):
        msg += f', is callable'
    return msg


logger = init_logger()
debug = logger.debug
info = logger.info
warning = logger.warn
error = logger.error
critical = logger.critical
